import pytest
from unittest.mock import patch
from APP.models.cinema_model import Hall, ScreeningSeat
from APP.models.movie_model import Movie,Screening
from APP.models.user_model import User
from APP.models.system_model import Booking, Payment,CreditCard,DebitCard,Coupon,Notification
from APP.general_controller import BookingSystem
from datetime import datetime

class TestHall:
    def setup_method(self):
        self.hall = Hall(1, "Hall 1", 100, ["seat1-1", "seat1-2", "seat1-3"])
    
    def test_hallID_getter(self):
        assert self.hall.hallID == 1

    def test_name_getter(self):
        assert self.hall.name == "Hall 1"

    def test_name_setter(self):
        self.hall.name = "New Hall Name"
        assert self.hall.name == "New Hall Name"

    def test_totalSeats_getter(self):
        assert self.hall.totalSeats == 100

    def test_totalSeats_setter(self):
        self.hall.totalSeats = 200
        assert self.hall.totalSeats == 200

    def test_listOfSeat_getter(self):
        expected_list = ["seat1-1", "seat1-2", "seat1-3"]
        assert self.hall.listOfSeat == expected_list

    def test_listOfSeat_setter(self):
        new_list = ["seat2-1", "seat2-2", "seat2-3"]
        self.hall.listOfSeat = new_list
        assert self.hall.listOfSeat == new_list

    def test_get_name_by_id(self, mocker):
        mocker.patch('APP.getCursor')
        db = Hall(1, 'Hall One', 100, ['seat1-1','seat1-2','seat1-3','seat1-4'])
        mocker.patch.object(db, 'get_name_by_id', return_value='Hall One')
        result = db.get_name_by_id(1)
        assert result == 'Hall One'

    def test_get_seatList(self,mocker):
        mocker.patch('APP.getCursor')
        db = Hall(1, 'Hall One', 100, ['seat1-1','seat1-2','seat1-3','seat1-4'])
        mocker.patch.object(db, 'get_seatList', return_value=['seat1-1','seat1-2','seat1-3','seat1-4'])
        result = db.get_seatList(1)
        assert result == ['seat1-1','seat1-2','seat1-3','seat1-4']

class TestScreeningSeat:
    def setup_method(self):
        self.screening_seat = ScreeningSeat(1, 2, "A1", 1, "available")

    def test_screeningSeatID_getter(self):
        assert self.screening_seat.screeningSeatID == 1

    def test_screeningID_getter(self):
        assert self.screening_seat.screeningID == 2

    def test_screeningID_setter(self):
        self.screening_seat.screeningID = 3
        assert self.screening_seat.screeningID == 3

    def test_seatNumber_getter(self):
        assert self.screening_seat.seatNumber == "A1"

    def test_seatNumber_setter(self):
        self.screening_seat.seatNumber = "B2"
        assert self.screening_seat.seatNumber == "B2"

    def test_hallID_getter(self):
        assert self.screening_seat.hallID == 1

    def test_hallID_setter(self):
        self.screening_seat.hallID = 2
        assert self.screening_seat.hallID == 2

    def test_status_getter(self):
        assert self.screening_seat.status == "available"

    def test_status_setter(self):
        self.screening_seat.status = "reserved"
        assert self.screening_seat.status == "reserved"   

class TestMovie:
    def setup_method(self):
        release_date = datetime(2023, 11, 2) 
        self.movie = Movie(1, "Movie Title", "Movie Description", 120, "English", release_date, "USA", "Action", "released")

    def test_movieID_getter(self):
        assert self.movie.movieID == 1

    def test_title_getter(self):
        assert self.movie.title == "Movie Title"

    def test_title_setter(self):
        self.movie.title = "New Movie Title"
        assert self.movie.title == "New Movie Title"

    def test_description_getter(self):
        assert self.movie.description == "Movie Description"

    def test_description_setter(self):
        self.movie.description = "New Movie Description"
        assert self.movie.description == "New Movie Description"

    def test_durationMins_getter(self):
        assert self.movie.durationMins == 120

    def test_durationMins_setter(self):
        self.movie.durationMins = 150
        assert self.movie.durationMins == 150

    def test_language_getter(self):
        assert self.movie.language == "English"

    def test_language_setter(self):
        self.movie.language = "Spanish"
        assert self.movie.language == "Spanish"

    def test_releaseDate_getter(self):
        assert self.movie.releaseDate == datetime(2023, 11, 2)  
    def test_releaseDate_setter(self):
        new_release_date = datetime(2024, 1, 1) 
        self.movie.releaseDate = new_release_date
        assert self.movie.releaseDate == new_release_date

    def test_country_getter(self):
        assert self.movie.country == "USA"

    def test_country_setter(self):
        self.movie.country = "Canada"
        assert self.movie.country == "Canada"

    def test_genre_getter(self):
        assert self.movie.genre == "Action"

    def test_genre_setter(self):
        self.movie.genre = "Drama"
        assert self.movie.genre == "Drama"

    def test_status_getter(self):
        assert self.movie.status == "released"

    def test_status_setter(self):
        self.movie.status = "upcoming"
        assert self.movie.status == "upcoming"

class TestScreening:
    def setup_method(self):
        date = datetime(2023, 11, 2)
        start_time = datetime(2023, 11, 2, 14, 0)
        end_time = datetime(2023, 11, 2, 16, 0)
        self.screening = Screening(1, 2, date, start_time, end_time, 1, 10.99, "active")

    def test_screeningID_getter(self):
        assert self.screening.screeningID == 1

    def test_movieID_getter(self):
        assert self.screening.movieID == 2

    def test_movieID_setter(self):
        self.screening.movieID = 3
        assert self.screening.movieID == 3

    def test_date_getter(self):
        expected_date = datetime(2023, 11, 2)
        assert self.screening.date == expected_date

    def test_date_setter(self):
        new_date = datetime(2023, 11, 3)
        self.screening.date = new_date
        assert self.screening.date == new_date

    def test_startTime_getter(self):
        expected_start_time = datetime(2023, 11, 2, 14, 0)
        assert self.screening.startTime == expected_start_time

    def test_startTime_setter(self):
        new_start_time = datetime(2023, 11, 2, 15, 0)
        self.screening.startTime = new_start_time
        assert self.screening.startTime == new_start_time

    def test_endTime_getter(self):
        expected_end_time = datetime(2023, 11, 2, 16, 0)
        assert self.screening.endTime == expected_end_time

    def test_endTime_setter(self):
        new_end_time = datetime(2023, 11, 2, 17, 0)
        self.screening.endTime = new_end_time
        assert self.screening.endTime == new_end_time

    def test_hallID_getter(self):
        assert self.screening.hallID == 1

    def test_hallID_setter(self):
        self.screening.hallID = 2
        assert self.screening.hallID == 2

    def test_price_getter(self):
        assert self.screening.price == 10.99

    def test_price_setter(self):
        self.screening.price = 9.99
        assert self.screening.price == 9.99

    def test_status_getter(self):
        assert self.screening.status == "active"

    def test_status_setter(self):
        self.screening.status = "inactive"
        assert self.screening.status == "inactive"

class TestUser:
    def setup_method(self):
        self.user = User(1, "testuser", "password123", "user", "John Doe", 1234567890, "123 Main St", "test@example.com")

    def test_userID_getter(self):
        assert self.user.userID == 1

    def test_username_getter(self):
        assert self.user.username == "testuser"

    def test_username_setter(self):
        self.user.username = "newuser"
        assert self.user.username == "newuser"

    def test_password_getter(self):
        assert self.user.password == "password123"

    def test_password_setter(self):
        self.user.password = "newpassword"
        assert self.user.password == "newpassword"

    def test_role_getter(self):
        assert self.user.role == "user"

    def test_role_setter(self):
        self.user.role = "admin"
        assert self.user.role == "admin"

    def test_name_getter(self):
        assert self.user.name == "John Doe"

    def test_name_setter(self):
        self.user.name = "Jane Doe"
        assert self.user.name == "Jane Doe"

    def test_phone_getter(self):
        assert self.user.phone == 1234567890

    def test_phone_setter(self):
        self.user.phone = 9876543210
        assert self.user.phone == 9876543210

    def test_address_getter(self):
        assert self.user.address == "123 Main St"

    def test_address_setter(self):
        self.user.address = "456 Elm St"
        assert self.user.address == "456 Elm St"

    def test_email_getter(self):
        assert self.user.email == "test@example.com"

    def test_email_setter(self):
        self.user.email = "new@example.com"
        assert self.user.email == "new@example.com"

class TestBooking:
    def setup_method(self):
        self.booking = Booking(1, 2, 3, datetime(2023, 11, 2), 4, ["seat1", "seat2"], 100.0, 5, "confirmed")

    def test_bookingID_getter(self):
        assert self.booking.bookingID == 1

    def test_userID_getter(self):
        assert self.booking.userID == 2

    def test_userID_setter(self):
        self.booking.userID = 6
        assert self.booking.userID == 6

    def test_numberOfSeat_getter(self):
        assert self.booking.numberOfSeat == 3

    def test_numberOfSeat_setter(self):
        self.booking.numberOfSeat = 4
        assert self.booking.numberOfSeat == 4

    def test_bookingDate_getter(self):
        assert self.booking.bookingDate == datetime(2023, 11, 2)

    def test_bookingDate_setter(self):
        new_date = datetime(2023, 11, 3)
        self.booking.bookingDate = new_date
        assert self.booking.bookingDate == new_date

    def test_screeningID_getter(self):
        assert self.booking.screeningID == 4

    def test_screeningID_setter(self):
        self.booking.screeningID = 7
        assert self.booking.screeningID == 7

    def test_seatList_getter(self):
        assert self.booking.seatList == ["seat1", "seat2"]

    def test_seatList_setter(self):
        new_seat_list = ["seat3", "seat4"]
        self.booking.seatList = new_seat_list
        assert self.booking.seatList == new_seat_list

    def test_amount_getter(self):
        assert self.booking.amount == 100.0

    def test_amount_setter(self):
        self.booking.amount = 150.0
        assert self.booking.amount == 150.0

    def test_paymentID_getter(self):
        assert self.booking.paymentID == 5

    def test_paymentID_setter(self):
        self.booking.paymentID = 8
        assert self.booking.paymentID == 8

    def test_status_getter(self):
        assert self.booking.status == "confirmed"

    def test_status_setter(self):
        self.booking.status = "canceled"
        assert self.booking.status == "canceled"

class TestCoupon:
    def setup_method(self):
        self.coupon = Coupon(1, datetime(2023, 11, 2), 0.1, "COUPON123")

    def test_couponID_getter(self):
        assert self.coupon.couponID == 1

    def test_couponID_setter(self):
        self.coupon.couponID = 2
        assert self.coupon.couponID == 2

    def test_expiryDate_getter(self):
        assert self.coupon.expiryDate == datetime(2023, 11, 2)

    def test_expiryDate_setter(self):
        new_date = datetime(2023, 11, 3)
        self.coupon.expiryDate = new_date
        assert self.coupon.expiryDate == new_date

    def test_discount_getter(self):
        assert self.coupon.discount == 0.1

    def test_discount_setter(self):
        self.coupon.discount = 0.2
        assert self.coupon.discount == 0.2

    def test_couponCode_getter(self):
        assert self.coupon.couponCode == "COUPON123"

    def test_couponCode_setter(self):
        new_code = "NEWCODE"
        self.coupon.couponCode = new_code
        assert self.coupon.couponCode == new_code

class TestPayment:
    def setup_method(self):
        self.payment = Payment(1, 100.0, datetime(2023, 11, 2), 2, 3, 4, "Success")

    def test_paymentID_getter(self):
        assert self.payment.paymentID == 1

    def test_paymentID_setter(self):
        self.payment.paymentID = 2
        assert self.payment.paymentID == 2

    def test_amount_getter(self):
        assert self.payment.amount == 100.0

    def test_amount_setter(self):
        self.payment.amount = 200.0
        assert self.payment.amount == 200.0

    def test_date_getter(self):
        assert self.payment.date == datetime(2023, 11, 2)

    def test_date_setter(self):
        new_date = datetime(2023, 11, 3)
        self.payment.date = new_date
        assert self.payment.date == new_date

    def test_couponID_getter(self):
        assert self.payment.couponID == 2

    def test_couponID_setter(self):
        self.payment.couponID = 3
        assert self.payment.couponID == 3

    def test_creditCardID_getter(self):
        assert self.payment.creditCardID == 3

    def test_creditCardID_setter(self):
        self.payment.creditCardID = 4
        assert self.payment.creditCardID == 4

    def test_debitCardID_getter(self):
        assert self.payment.debitCardID == 4

    def test_debitCardID_setter(self):
        self.payment.debitCardID = 5
        assert self.payment.debitCardID == 5

    def test_status_getter(self):
        assert self.payment.status == "Success"

    def test_status_setter(self):
        new_status = "Failed"
        self.payment.status = new_status
        assert self.payment.status == new_status

class TestCreditCard:
    def setup_method(self):
        self.creditcard = CreditCard(1, "1234 5678 1234 5678", "Visa", "12/25", "John Doe", "123")

    def test_creditcardID_getter(self):
        assert self.creditcard.creditcardID == 1

    def test_cardNumber_getter(self):
        assert self.creditcard.cardNumber == "1234 5678 1234 5678"

    def test_cardNumber_setter(self):
        self.creditcard.cardNumber = "9876 5432 9876 5432"
        assert self.creditcard.cardNumber == "9876 5432 9876 5432"

    def test_cardType_getter(self):
        assert self.creditcard.cardType == "Visa"

    def test_cardType_setter(self):
        self.creditcard.cardType = "MasterCard"
        assert self.creditcard.cardType == "MasterCard"

    def test_expiryDate_getter(self):
        assert self.creditcard.expiryDate == "12/25"

    def test_expiryDate_setter(self):
        new_expiry_date = "05/24"
        self.creditcard.expiryDate = new_expiry_date
        assert self.creditcard.expiryDate == new_expiry_date

    def test_nameOnCard_getter(self):
        assert self.creditcard.nameOnCard == "John Doe"

    def test_nameOnCard_setter(self):
        self.creditcard.nameOnCard = "Jane Smith"
        assert self.creditcard.nameOnCard == "Jane Smith"

    def test_securityNumber_getter(self):
        assert self.creditcard.securityNumber == "123"

    def test_securityNumber_setter(self):
        self.creditcard.securityNumber = "456"
        assert self.creditcard.securityNumber == "456"

class TestDebitCard:
    def setup_method(self):
        self.debitcard = DebitCard(1, "1234 5678 1234 5678", "Bank of Example", "John Doe")

    def test_debitcardID_getter(self):
        assert self.debitcard.debitcardID == 1

    def test_cardNumber_getter(self):
        assert self.debitcard.cardNumber == "1234 5678 1234 5678"

    def test_cardNumber_setter(self):
        self.debitcard.cardNumber = "9876 5432 9876 5432"
        assert self.debitcard.cardNumber == "9876 5432 9876 5432"

    def test_bankName_getter(self):
        assert self.debitcard.bankName == "Bank of Example"

    def test_bankName_setter(self):
        self.debitcard.bankName = "Another Bank"
        assert self.debitcard.bankName == "Another Bank"

    def test_nameOnCard_getter(self):
        assert self.debitcard.nameOnCard == "John Doe"

    def test_nameOnCard_setter(self):
        self.debitcard.nameOnCard = "Jane Smith"
        assert self.debitcard.nameOnCard == "Jane Smith"

class TestNotification:
    def setup_method(self):
        self.notification = Notification(1, "2023-11-02", "Sample content", 100)

    def test_notificationID_getter(self):
        assert self.notification.notificationID == 1

    def test_date_getter(self):
        assert self.notification.date == "2023-11-02"

    def test_date_setter(self):
        self.notification.date = "2023-11-03"
        assert self.notification.date == "2023-11-03"

    def test_content_getter(self):
        assert self.notification.content == "Sample content"

    def test_content_setter(self):
        self.notification.content = "Updated content"
        assert self.notification.content == "Updated content"

    def test_userID_getter(self):
        assert self.notification.userID == 100

    def test_userID_setter(self):
        self.notification.userID = 200
        assert self.notification.userID == 200

class MockCurrentUser:
    def is_authenticated(self):
        return True

    def get_id(self):
        return 1  # Replace with the user ID you expect

class MockMovie:
    @staticmethod
    def get_movie_list():
        # Define the expected movie list here
        return ["Movie 1", "Movie 2", "Movie 3"]

if __name__ == "__main":
    pytest.main()
