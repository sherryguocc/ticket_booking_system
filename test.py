import pytest
from APP.models.cinema_model import Hall, ScreeningSeat

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

if __name__ == "__main":
    pytest.main()
