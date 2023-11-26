from flask import *
from DBConnection import Db

app = Flask(__name__)
app.secret_key = "whub"


# ===================== user ====================

@app.route('/')
def home():
    lid = session.get('lid')
    if lid is None:
        return redirect('/login')
    db = Db()
    # qry = "SELECT product_id, name, price, image FROM products"
    # res = db.select(qry)
    # products = []
    # for row in res:
    #     product = {
    #         'product_id': row['product_id'],
    #         'name': row['name'],
    #         'price': row['price'],
    #         'image': row['image']
    #     }
    #     products.append(product)
    qry1 = "SELECT name FROM signup WHERE  uid = '" + lid + "' "
    user_res = db.selectOne(qry1)
    if user_res is None:
        return redirect("/login")
    user_name = user_res['name']
    return render_template("home.html", user_name=user_name)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login-post', methods=['POST'])
def login_post():
    # email = request.form['email']
    # passw = request.form['password']
    # db = Db()
    # qry = "select * from login where email = '" + email + "' and password='" + passw + "'"
    # res = db.selectOne(qry)
    # if res is None:
    #     return '''<script>alert("Invalid Username Or Password");window.location="/"</script>'''
    # else:
    #     session["lid"] = str(res['lid'])
    #     return redirect('/')

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

@app.route('/logout-post',methods=['GET'])
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
    return render_template('view.html')


@app.route('/view-get', methods=['GET'])
def view_get():
    return render_template('view.html')


@app.route('/forgot')
def forgot():
    return render_template('forgotpassword.html')


@app.route('/add')
def add():
    return render_template('addpost.html')


@app.route('/add-post', methods=['POST'])
def add_post():
    return render_template('addpost.html')


# ===============================================

# ==================== admin ====================


@app.route('/admin')
def admin():
    lid = session.get('lid')
    if lid is None:
        return redirect('/login')
    db = Db()
    # qry = "SELECT product_id, name, price, image FROM products"
    # res = db.select(qry)
    # products = []
    # for row in res:
    #     product = {
    #         'product_id': row['product_id'],
    #         'name': row['name'],
    #         'price': row['price'],
    #         'image': row['image']
    #     }
    #     products.append(product)
    qry1 = "SELECT name FROM signup WHERE  uid = '" + lid + "' "
    user_res = db.selectOne(qry1)
    if user_res is None:
        return redirect("/login")
    user_name = user_res['name']
    return render_template("admin.html", user_name=user_name)




# ===============================================

if __name__ == '__main__':
    app.run(debug=True)
