import pytest
from APP.models.cinema_model import Hall, ScreeningSeat
from APP.models.movie_model import Movie,Screening
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

if __name__ == "__main":
    pytest.main()
