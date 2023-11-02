from flask import Blueprint, render_template, redirect, url_for, flash, request
from APP.general_controller import BookingSystem
from flask_login import (UserMixin, LoginManager, login_user, login_required, logout_user, current_user)


# Create a Blueprint for the admin routes
admin = Blueprint('admin', __name__)

@admin.route('/admin/add_screening', methods=['GET','POST'])
@login_required
def add_screening():
    movieList = BookingSystem.get_movie_list()
    if request.method == 'POST':
        search_content = request.form['search_content']
        movies = BookingSystem.search_movies(search_content)
        return render_template ('admin/add_screening.html', movies=movies, search_content=search_content)
    return render_template('admin/add_screening.html',movieList=movieList)

@admin.route('/admin/add_screening_by_id/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def add_screening_by_id(movie_id):
    movie_name= BookingSystem.get_movie_name_by_movie_id(movie_id)
    if request.method == 'POST':
        screening_date = request.form.get('screening_date')
        startTime = request.form.get('start_time')
        hallID = request.form.get('hall')
        price = float(request.form.get('price'))
        BookingSystem.add_screening(movie_id, screening_date, startTime, hallID, price) 
    return render_template('admin/add_screening_by_id.html', movie_id=movie_id, movie_name=movie_name)

@admin.route('/admin/add_movie', methods=['GET', 'POST'])
@login_required
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        duration_mins = request.form.get('duration_mins')
        language = request.form.get('language')
        if language == 'Other':
            language = request.form.get('language-input')
        country = request.form.get('country')
        if country == 'Other':
            country = request.form.get('country-input')
        genre = request.form.get('genre')
        if genre == 'Other':
            genre = request.form.get('genre-input')

        release_year = request.form.get('release_year')
        release_month = request.form.get('release_month')
        release_day = request.form.get('release_day')
        release_date = f"{release_year}-{release_month}-{release_day}"

        BookingSystem.add_movie(title, description, duration_mins, language, release_date, country, genre)
        flash("Movie added successfully.")
        return redirect(url_for('home.home'))

    return render_template('admin/add_movie.html')

@admin.route('/admin/cancel_screening', methods=['GET','POST'])
@login_required
def cancel_screening():
    movieList = BookingSystem.get_movie_list()
    if request.method == 'POST':
        search_content = request.form['search_content']
        movies = BookingSystem.search_movies(search_content)
        return render_template ('admin/cancel_screening.html', movies=movies, search_content=search_content)
    return render_template('admin/cancel_screening.html',movieList=movieList)

@admin.route('/admin/cancel_screening_by_id/<int:screening_id>/<int:movie_id>')
@login_required
def cancel_screening_by_id(screening_id,movie_id):
    BookingSystem.cancel_screening(screening_id)
    return redirect(url_for('home.screening_list', movie_id=movie_id))

@admin.route('/admin/cancel_movie')
@login_required
def cancel_movie():
    movieList = BookingSystem.get_movie_list()
    if request.method == 'POST':
        search_content = request.form['search_content']
        movies = BookingSystem.search_movies(search_content)
        return render_template ('admin/cancel_movie.html', movies=movies, search_content=search_content)
    return render_template('admin/cancel_movie.html',movieList=movieList)

@admin.route('/admin/cancel_movie_by_id/<int:movie_id>')
@login_required
def cancel_movie_by_id(movie_id):
    BookingSystem.cancel_movie(movie_id)
    return redirect(url_for('home.home', movie_id=movie_id))
    

