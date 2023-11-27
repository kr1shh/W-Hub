from datetime import datetime
from flask import *
from DBConnection import Db
import os

app = Flask(__name__)
app.secret_key = "whub"

# ===================== user ====================

@app.route('/')
def home():
    lid = session.get('lid')
    if lid is None:
        return redirect('/login')
    db = Db()
    qry = "SELECT groupname, groupdes, grouplink, groupdp, gid FROM `groups`"
    res = db.select(qry)
    groups = []
    for row in res:
        group = {
            'gid': row['gid'],
            'name': row['groupname'],
            'des': row['groupdes'],
            'url': row['grouplink'],
            'dp': row['groupdp']
        }
        groups.append(group)

    qry1 = "SELECT name FROM signup WHERE  uid = '" + lid + "' "
    user_res = db.selectOne(qry1)
    if user_res is None:
        return redirect("/login")
    user_name = user_res['name']
    return render_template("home.html", user_name=user_name, groups=groups)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login-post', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    db = Db()

    qry = "SELECT * FROM login WHERE email = '" + email + "' AND password = '" + password + "'"
    res = db.selectOne(qry)

    if res is None:
        return '''<script>alert("Invalid Username Or Password");window.location="/"</script>'''
    else:
        if res['type'] == 'user':
            session['lid'] = str(res['lid'])
            return redirect('/')
        elif res['type'] == 'admin':
            session['lid'] = str(res['lid'])
            return redirect('/admin')


@app.route('/logout-post', methods=['GET'])
def logout():
    session.clear()
    return redirect('/login')


@app.route('/signup')
def sign_up():
    return render_template('signup.html')


@app.route('/signup-post', methods=['POST'])
def signup_post():
    db = Db()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        type = request.form['type']
        qry1 = "INSERT INTO login (email,password,type) VALUES('" + email + "','" + password + "','" + type + "')"
        res = db.insert(qry1)
        lid = str(res)
        qry2 = "INSERT INTO signup (uid,name) VALUES('" + lid + "','" + name + "')"
        db.insert(qry2)

    else:
        return '''<script>alert(" Register via the signup form ");window.location="/"</script>'''

    return redirect('/login')


@app.route('/view')
def view():
    lid = session.get('lid')
    if lid is None:
        return redirect('/login')
    gid = request.args.get('groupID')
    db = Db()
    qry = " SELECT * FROM `groups` WHERE gid = '" + gid + "' "
    res = db.select(qry)
    if not res:
        return "Group not found"

    group_info = res[0]

    dp = group_info.get('groupdp')
    name = group_info.get('groupname')
    des = group_info.get('groupdes')
    url = group_info.get('grouplink')

    qry1 = "SELECT name FROM signup WHERE  uid = '" + lid + "' "
    user_res = db.selectOne(qry1)
    if user_res is None:
        return redirect("/login")
    user_name = user_res['name']
    return render_template('view.html', user_name=user_name, dp=dp, name=name, des=des, url=url)


@app.route('/view-get', methods=['GET'])
def view_get():
    return render_template('view.html')


@app.route('/forgot')
def forgot():
    return render_template('forgotpassword.html')


@app.route('/add')
def add():
    lid = session.get('lid')
    if lid is None:
        return redirect('/login')
    db = Db()
    qry1 = "SELECT name FROM signup WHERE  uid = '" + lid + "' "
    user_res = db.selectOne(qry1)
    if user_res is None:
        return redirect("/login")
    user_name = user_res['name']
    return render_template("addpost.html", user_name=user_name)


@app.route('/delete', methods=['GET'])
def delete():
    gid = request.args.get('groupID')
    db = Db()
    qry1 = " SELECT groupdp FROM `groups` WHERE gid = '" + gid + "' "
    dp = db.selectOne(qry1)
    icon = dp['groupdp']

    if icon:
        try:
            os.remove(icon)
        except OSError:
            pass

    qry = "DELETE FROM `groups` WHERE gid = '" + gid + "'"
    db.delete(qry)
    return  ''' <script>alert("Deletion completed");window.location="/admin"</script> '''





# ===============================================

# ==================== admin ====================

@app.route('/admin')
def admin():
    lid = session.get('lid')
    if lid is None:
        return redirect('/login')
    db = Db()
    qry = "SELECT groupname, groupdes, grouplink, groupdp, gid FROM `groups`"
    res = db.select(qry)
    groups = []
    for row in res:
        group = {
            'gid': row['gid'],
            'name': row['groupname'],
            'des': row['groupdes'],
            'url': row['grouplink'],
            'dp': row['groupdp']
        }
        groups.append(group)
    qry1 = "SELECT name FROM signup WHERE  uid = '" + lid + "' "
    user_res = db.selectOne(qry1)
    if user_res is None:
        return redirect("/login")
    user_name = user_res['name']
    return render_template("admin.html", user_name=user_name, groups=groups)


@app.route('/add-post', methods=['POST'])
def add_post():
    lid = session.get("lid")
    name = request.form['group-name']
    url = request.form['group-url']
    des = request.form['group-des']
    image = request.files['group-dp']
    if image:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{current_time}_{image.filename}"
        image_url = os.path.join('static/assets/posts', filename)
        image_path = os.path.join('../static/assets/posts/', filename)
        os.makedirs('static/assets/posts', exist_ok=True)
        image.save(image_url)
        print(image_path)
    else:
        return '''<script>alert("Upload an image also");window.location="/add-product"</script>'''
    db = Db()
    qry = f"INSERT INTO `groups` (uid, groupname, groupdes, grouplink, groupdp) VALUES ('{lid}', '{name}', '{des}', '{url}', '{image_path}')"
    db.insert(qry)
    return '"<script>alert("Groupe added successfully");window.location="/add"</script>"'


# ===============================================

if __name__ == '__main__':
    app.run(debug=True)
