
from flask import Blueprint, render_template, redirect, url_for, flash, request
from APP.general_controller import BookingSystem
from flask_login import (UserMixin, LoginManager, login_user, login_required, logout_user, current_user)
from datetime import datetime

customer =  Blueprint('customer', __name__)

@customer.route('/make_booking/<int:screening_id>')
@login_required
def make_booking(screening_id):
    user_id = current_user.get_id()
    movie_name = BookingSystem.get_movie_name(screening_id)
    screening = BookingSystem.get_screening(screening_id)
    seatList = BookingSystem.get_screening_seats(screening_id)
    booked_seats = BookingSystem.get_booked_seats(screening_id)
    reserved_seats = BookingSystem.get_reserved_seats(screening_id)
    all_seats = BookingSystem.get_screening_seats(screening_id)
    rows = BookingSystem.get_screening_seats_row(screening_id)
    columns = BookingSystem.get_screening_seats_column(screening_id)
    return render_template('customer/make_booking.html', 
                           user_id=user_id,
                           movie_name = movie_name,
                           screening_id=screening_id, 
                           screening=screening,
                           seatList=seatList, reserved_seats=reserved_seats,
                           booked_seats =booked_seats, all_seats=all_seats,
                           rows=rows, columns=columns)

@customer.route('/confirm_booking/<int:screening_id>', methods=['GET','POST'])
@login_required
def confirm_booking(screening_id):
    user_id = current_user.get_id()
    selected_seats = [seat for seat in request.form.getlist('selected_seats') if seat.strip()]
    selected_screening = BookingSystem.get_screening(screening_id)
    seats_count = BookingSystem.count_seats(selected_seats)
    total_amount = BookingSystem.total_amount(selected_seats, screening_id)
    movie_name = BookingSystem.get_movie_name(screening_id)
    
    return render_template('customer/confirm_booking.html', 
                       selected_seats=selected_seats,
                       selected_screening=selected_screening,
                       screening_id=screening_id, 
                       seats_count=seats_count, total_amount=total_amount,
                       movie_name=movie_name,
                       user_id=user_id)

@customer.route('/add_booking/<int:screening_id>', methods=['POST'])
@login_required
def add_booking(screening_id):
    user_id = current_user.get_id()
    selected_seats = request.form.getlist('selected_seats')
    seats_info = selected_seats[0] 
    seat_list = seats_info.split(', ')
    new_booking = BookingSystem.add_booking(user_id, screening_id, seat_list)
    if new_booking:
        flash('Booking successful!')
        return redirect(url_for('customer.booking_list',user_id=user_id))
    else:
        flash('Error happens while adding booking!')
        return redirect(url_for('customer.make_booking',screening_id=screening_id))
        
@customer.route('/credicard/<int:booking_id>', methods=['GET','POST'])
@login_required
def pay_by_creditcard(booking_id):
    user_id = current_user.get_id()
    if request.method == "POST":
        coupon = request.form.get('coupon')

        card_number = request.form.get('cardNumber')
        card_type = request.form.get('cardType')
        name_on_card = request.form.get('nameOnCard')
        security_number = request.form.get('securityNumber')

        expiry_month = request.form.get('expiryMonth')
        expiry_year = request.form.get('expiryYear')
        expiry_date = f"{expiry_month}/{expiry_year}"

        date=datetime.now()

        card_id = BookingSystem.add_creditcard_return_id(card_number,card_type,expiry_date,name_on_card,security_number)
        payment_id = BookingSystem.add_payment_return_id(booking_id,date,coupon,card_id,None)
        BookingSystem.pay_for_booking(booking_id, payment_id)
        flash("booking paid successfully!")
        return redirect(url_for('customer.booking_list',user_id=user_id))

    return render_template('customer/creditcard.html',booking_id=booking_id, user_id=user_id)


@customer.route('/debitcard/<int:booking_id>', methods=['GET','POST'])
@login_required
def pay_by_debitcard(booking_id):
    if request.method == "POST":
        user_id = current_user.get_id()
        date=datetime.now()
        coupon = request.form.get('coupon')
        card_number = request.form.get('cardNumber')
        bank_name = request.form.get('bankName')
        name_on_card = request.form.get('nameOnCard')
        card_id = BookingSystem.add_debitcard_return_id(card_number,bank_name,name_on_card)
        print("car_id get:",card_id)
        payment_id = BookingSystem.add_payment_return_id(booking_id,date,coupon,None,card_id)
        print("payment_id get:",payment_id)
        BookingSystem.pay_for_booking(booking_id, payment_id)
        return redirect(url_for('customer.booking_list',user_id=user_id))
    return render_template('customer/debitcard.html',booking_id=booking_id)

@customer.route('/cash', methods=['GET','POST'])
@login_required
def pay_by_cash():
    return render_template('customer/cash.html')

@customer.route('/booking_list.html/<int:user_id>', methods=['GET','POST'])
@login_required
def booking_list(user_id):
    user_id = current_user.get_id()
    bookingList = BookingSystem.get_booking_list_with_details(user_id)

    return render_template('customer/booking_list.html', user_id=user_id, bookingList=bookingList)

@customer.route('/cancel_booking/<int:booking_id>', methods=['POST'])
@login_required
def cancel_booking(booking_id):
    user_id = current_user.get_id()
    print("booking_id in view:",booking_id)
    BookingSystem.cancel_booking(booking_id)
    return redirect(url_for('customer.booking_list', user_id=user_id))

@customer.route('/customer/pay/<int:booking_id>/<payment_method>')
def pay(booking_id, payment_method):
    user_id = current_user.get_id()
    if payment_method == 'credit_card':
        return render_template('customer/creditcard.html', booking_id=booking_id, user_id=user_id)
    elif payment_method == 'debit_card':
        return render_template('customer/debitcard.html', booking_id=booking_id, user_id=user_id)
    elif payment_method == 'cash':
        return render_template('customer/cash.html',user_id=user_id)
    

@customer.route('/customer/notifications/<int:user_id>/')
def get_notifications(user_id):
    notification_list = BookingSystem.get_notifications(user_id)
    return render_template('customer/notifications.html', notification_list=notification_list)
