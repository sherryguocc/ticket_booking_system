import unittest
from unittest.mock import patch, MagicMock
from APP.models.cinema_model import Hall, ScreeningSeat
import json

# Import Hall class and any other necessary dependencies

class TestHallMethods(unittest.TestCase):
    def setUp(self):
        self.hall = Hall(1, "Hall 1", 100, ["seat1-1", "seat1-2", "seat1-3"])
    
    def test_hallID_getter(self):
        self.assertEqual(self.hall.hallID, 1)

    def test_name_getter(self):
        self.assertEqual(self.hall.name, "Hall 1")

    def test_name_setter(self):
        self.hall.name = "New Hall Name"
        self.assertEqual(self.hall.name, "New Hall Name")

    def test_totalSeats_getter(self):
        self.assertEqual(self.hall.totalSeats, 100)

    def test_totalSeats_setter(self):
        self.hall.totalSeats = 200
        self.assertEqual(self.hall.totalSeats, 200)

    def test_listOfSeat_getter(self):
        expected_list = ["seat1-1", "seat1-2", "seat1-3"]
        self.assertEqual(self.hall.listOfSeat, expected_list)

    def test_listOfSeat_setter(self):
        new_list = ["seat2-1", "seat2-2", "seat2-3"]
        self.hall.listOfSeat = new_list
        self.assertEqual(self.hall.listOfSeat, new_list)

    def test_get_name_by_id(self):
        # Mock the getCursor function to return a mock cursor
        with patch('APP.models.cinema_model.getCursor') as mock_getCursor:
            # Set up the mock cursor and connection behavior
            mock_connection = mock_getCursor.return_value
            mock_connection.fetchone.return_value = (1, "Hall 1", 100, "[1, 2, 3, 4]")

            # Create a Hall instance
            hall = Hall(1, "Hall 1", 100, [1, 2, 3, 4])

            # Test the get_name_by_id method
            result = hall.get_name_by_id(1)
            self.assertEqual(result, "Hall 1")

    @patch('APP.models.cinema_model.getCursor')
    def test_get_seatList(self, mock_getCursor):
        mock_cursor = mock_getCursor.return_value
        data = ("1", "Hall One", "4", ["seat1-1", "seat1-2", "seat1-3", "seat1-4"])
        data = data[:3] + (json.dumps(data[3]),)
        mock_cursor.fetchone.return_value = data
        test_result = Hall.get_seatList(1)

        expected_result = ["seat1-1", "seat1-2", "seat1-3", "seat1-4"]
        self.assertEqual(test_result, expected_result)

if __name__ == '__main__':
    unittest.main()

class TestScreeningSeatAttributes(unittest.TestCase):
    def setUp(self):
        self.screening_seat = ScreeningSeat(1, 1, "A1", 1, "available")
    
    def test_screeningSeatID_getter(self):
        self.assertEqual(self.screening_seat.screeningSeatID, 1)

    def test_screeningID_getter(self):
        self.assertEqual(self.screening_seat.screeningID, 1)

    def test_screeningID_setter(self):
        self.screening_seat.screeningID = 2
        self.assertEqual(self.screening_seat.screeningID, 2)

    def test_seatNumber_getter(self):
        self.assertEqual(self.screening_seat.seatNumber, "A1")

    def test_seatNumber_setter(self):
        self.screening_seat.seatNumber = "B2"
        self.assertEqual(self.screening_seat.seatNumber, "B2")

    def test_hallID_getter(self):
        self.assertEqual(self.screening_seat.hallID, 1)

    def test_hallID_setter(self):
        self.screening_seat.hallID = 2
        self.assertEqual(self.screening_seat.hallID, 2)

    def test_status_getter(self):
        self.assertEqual(self.screening_seat.status, "available")

    def test_status_setter(self):
        self.screening_seat.status = "booked"
        self.assertEqual(self.screening_seat.status, "booked")

if __name__ == '__main__':
    unittest.main()


