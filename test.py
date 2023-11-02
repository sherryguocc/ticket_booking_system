import pytest
from APP.models.cinema_model import Hall, ScreeningSeat
from APP.models.movie_model import Movie,Screening
from APP.models.user_model import User
from APP.models.system_model import Booking, Payment,CreditCard,DebitCard,Coupon,Notification
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

if __name__ == "__main":
    pytest.main()
