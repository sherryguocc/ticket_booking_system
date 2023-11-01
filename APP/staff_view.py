from flask import Blueprint, render_template, redirect, url_for, flash, request
from APP.general_controller import BookingSystem
from flask_login import (UserMixin, LoginManager, login_user, login_required, logout_user, current_user)
from datetime import datetime

staff =  Blueprint('staff', __name__)

@staff.route('/add_coupon', methods=['GET','POST'])
@login_required
def add_coupon():
    coupon_list= BookingSystem.display_coupon_list()
    if request.method == 'POST':
        expiry_date = request.form.get('expiry_date')
        discount = request.form.get('discount')
        success = BookingSystem. add_coupon(expiry_date,discount)
        if success:
            flash('Coupon added succesfully!')
            return redirect (url_for('staff.add_coupon'))
        else:
            flash('failed to add coupon, please try again!')
            return redirect (url_for('staff.add_coupon'))
    return render_template('staff/add_coupon.html',coupon_list=coupon_list)