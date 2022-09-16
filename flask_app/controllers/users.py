from flask_app import app
from flask import render_template, redirect, request, session,flash
from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# CREATE 

@app.route('/users/register', methods=['POST'])
def register_user():

    if not User.validate_register(request.form):
        return redirect('/users/register')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.create_user(data)
    return redirect('/users/account')

@app.route('/users/login', methods=['POST'])
def login_user():
    this_user = User.read_by_email({"email": request.form['email']})
    if not this_user:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = this_user.id
    return redirect('/users/account')

# READ 

@app.route('/')
def index():
    return render_template("homepage.html")