from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# CREATE 

@app.route('/users/register', methods=['POST'])
def register_user():

    if not User.validate_register(request.form):
        return redirect('/user/signup')
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
        return redirect('/user/login')
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = this_user.id
    return redirect('/users/account')


# READ 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/account')
def user_account():
    return render_template("user_account.html")

@app.route('/new_here/')
def visitor_page():
    return render_template("new_visitor.html")

@app.route('/our_history/')
def about_page():
    return render_template("about_us.html")

@app.route('/our_team/')
def our_team():
    return render_template("our_team.html")

@app.route('/user/signup')
def user_signup():
    return render_template("register_account.html")

@app.route('/user/login')
def user_login():
    return render_template("login_account.html")

@app.route('/contact')
def contact_info():
    return render_template("contact.html")

@app.route('/adults')
def adults_info():
    return render_template("adults.html")

@app.route('/youth')
def youth_info():
    return render_template("youth.html")

@app.route('/events/costume-party')
def costume_event():
    return render_template("costume_party.html")

@app.route('/events/christmas-party')
def christmas_party():
    return render_template("christmas_party.html")

@app.route('/events/ski-trip')
def ski_trip():
    return render_template("ski_trip.html")

@app.route('/children')
def children_info():
    return render_template("children.html")

@app.route('/missions')
def missions_info():
    return render_template("missions.html")

@app.route('/watch_listen/')
def watch_listen():
    return render_template("watch_listen.html")

@app.route('/events')
def event_info():
    return render_template("events.html")

@app.route('/give')
def give_info():
    return render_template("give.html")

@app.route('/bible_studies/')
def bible_studies():
    return render_template("bible_studies.html")

    
@app.route('/user/logout')
def logout():
    session.pop("user_id")
    return redirect('/')