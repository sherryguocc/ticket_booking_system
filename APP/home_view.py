
from flask import Blueprint, render_template, redirect, url_for, flash, request
from APP.general_controller import BookingSystem
from flask_login import (UserMixin, LoginManager, login_user, login_required, logout_user, current_user)


bp = Blueprint('home', __name__)

# Display the movie list on the home page
@bp.route('/')
def home():
    movieList, user_id = BookingSystem.show_home()
    return render_template('base.html', movieList=movieList, user_id=user_id)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = BookingSystem.login(username, password)
        if user:
            login_user(user)
            return redirect(url_for('home.home'))
        else:
            flash('Invalid credentials. Please check your username and password.', 'error')
    return render_template('login.html')

# Register route
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        if not phone:
            phone  =None
        if not address:
            address= None
        BookingSystem.register(username,password,name,email,phone,address)
        return redirect(url_for('home.login'))
    return render_template('register.html')

@login_required
@bp.route('/logout')
def logout():
    return BookingSystem.logout()

@bp.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_content = request.form['search_content']
        movies = BookingSystem.search_movies(search_content)
        if movies:
            return render_template('base.html', movies=movies, search_content=search_content)
        else:
            flash('Cannot find movie!')
            return redirect(url_for('home.home'))
        
@bp.route('/screening_list/<int:movie_id>')
def screening_list(movie_id):
    screeningList = BookingSystem.screening_list_display(movie_id)
    return render_template('screening_list.html', screeningList=screeningList, movie_id=movie_id)

