from flask import *

app = Flask (__name__)
app.secret_key = "wstore"

#===================== user ====================

@app.route('/')
def test():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login-post', methods=['POST'])
def login_post():
    return render_template('login.html')


@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/signup-post',methods=['POST'])
def signup_post():
    return render_template('signup.html')


@app.route('/view')
def view():
    return render_template('view.html')



@app.route('/view-get',methods=['GET'])
def view_get():
    return render_template('view.html')


@app.route('/forgot')
def forgot():
    return render_template('forgotpassword.html')

@app.route('/add')
def add():
    return render_template('addpost.html')

@app.route('/add-post',methods=['POST'])
def add_post():
    return render_template('addpost.html')



#===============================================

#==================== admin ====================


@app.route('/admin')
def admin():
    return render_template('admin.html')


#===============================================

if __name__ == '__main__' :
    app.run(debug=True)


