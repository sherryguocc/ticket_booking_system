from flask import Blueprint, render_template, redirect, url_for, flash, request
from APP.general_controller import BookingSystem
from flask_login import (UserMixin, LoginManager, login_user, login_required, logout_user, current_user)
from datetime import datetime

staff =  Blueprint('staff', __name__)

@staff.route('/add_coupon')
@login_required
def add_coupon():
    pass