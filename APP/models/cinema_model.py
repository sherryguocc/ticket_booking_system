from APP import getCursor
import json

class Hall:
    def __init__(self, hallID, name, totalSeats, listOfSeat):
        self.__hallID = hallID
        self.__name = name
        self.__totalSeats = totalSeats
        self.__listOfSeat = listOfSeat
    
    # Property getters and setters for various attributes.
    # These allow controlled access to the private attributes.
    
    @property
    def hallID (self):
        return self.__hallID
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def totalSeats(self):
        return self.__totalSeats
    
    @totalSeats.setter
    def totalSeats(self, totalSeats):
        self.__totalSeats = totalSeats

    @property
    def listOfSeat(self):
        return self.__listOfSeat
    
    @listOfSeat.setter
    def listOfSeat(self, listOfSeat):
        self.__listOfSeat = listOfSeat
    
    @staticmethod
    def get_name_by_id(hall_id):
        connection = getCursor()
        query = """ SELECT * FROM hall WHERE hallID = %s """
        connection.execute(query,(hall_id,))
        hall = connection.fetchone()
        name = hall[1]
        return name
    
    @staticmethod
    def get_seatList(hall_id):
        connection = getCursor()
        query = """ SELECT listOfSeat FROM hall WHERE hallID = %s """
        connection.execute(query,(hall_id,))
        seats = connection.fetchone()
        seats_json = seats[0]  # 'seats' is a tuple, so access the JSON string at index 0
        # Parse JSON string to Python list
        seats_list = json.loads(seats_json)
        return seats_list

class ScreeningSeat:
    def __init__(self, screeningSeatID, screeningID, seatNumber, hallID, status):
        self.__screeningSeatID = screeningSeatID
        self.__screeningID = screeningID
        self.__seatNumber = seatNumber
        self.__hallID =hallID
        self.__status= status

    @property
    def screeningSeatID(self):
        return self.__screeningSeatID

    @property
    def screeningID(self):
        return self.__screeningID

    @screeningID.setter
    def screeningID(self, value):
        self.__screeningID = value

    @property
    def seatNumber(self):
        return self.__seatNumber

    @seatNumber.setter
    def seatNumber(self, value):
        self.__seatNumber = value

    @property
    def hallID(self):
        return self.__hallID

    @hallID.setter
    def hallID(self, value):
        self.__hallID = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    
    @staticmethod
    def add_seats(screening_id, hall_id):
        try:
            query = """INSERT INTO screeningseat (screeningID, seatNumber, hallID, status) VALUES (%s, %s, %s, %s)"""
            status = 'available'
            seatList = Hall.get_seatList(hall_id)

            for seatNumber in seatList:
                values = (screening_id, seatNumber, hall_id, status)
                with getCursor() as connection:
                    connection.execute(query, values)
            return True         
        except Exception as e:
            print("Error while adding screening:", e)
            return False    
    
    @staticmethod
    def get_seats(screening_id):
        connection = getCursor()
        query = """SELECT seatNumber FROM screeningseat WHERE screeningID = %s"""
        connection.execute(query, (screening_id,))
        results = connection.fetchall()
        seats = [result[0] for result in results]
        return seats
    
    @staticmethod
    def get_booked_seats(screening_id):
        connection = getCursor()
        query = """SELECT seatNumber FROM screeningseat WHERE screeningID = %s AND status = 'booked'"""
        connection.execute(query, (screening_id,))
        results = connection.fetchall()
        booked_seats = [result[0] for result in results]
        return booked_seats
    
    @staticmethod
    def get_reserved_seats(screening_id):
        connection = getCursor()
        query = """SELECT seatNumber FROM screeningseat WHERE screeningID = %s AND status = 'reserved'"""
        connection.execute(query, (screening_id,))
        results = connection.fetchall()
        reserved_seats = [result[0] for result in results]
        return reserved_seats
    
    @staticmethod
    def book_seat(screening_id, seat_number):
        connection = getCursor()
        update_query = """UPDATE screeningseat SET status='booked' WHERE screeningID = %s AND seatNumber = %s"""
        connection.execute(update_query, (screening_id, seat_number))

    @staticmethod
    def get_max_rows_and_columns(screening_id):
        connection = getCursor()
        query = """SELECT seatNumber FROM screeningseat WHERE screeningID = %s"""
        connection.execute(query, (screening_id,))
        results = connection.fetchall()
     
        max_row = 0
        max_column = 0
        for result in results:
            seat_number = result[0]
            parts = seat_number.split('-')
            if len(parts) == 2:
                row = int(parts[0].replace("seat", ""))
                column = int(parts[1])
                if row > max_row:
                    max_row = row
                if column > max_column:
                    max_column = column
        
        return max_row, max_column
    
    @staticmethod
    def cancel_seat(screening_id, seat_number):
        connection = getCursor()
        update_query = """UPDATE screeningseat SET status='available' WHERE screeningID = %s AND seatNumber = %s"""
        connection.execute(update_query, (screening_id, seat_number))
    
    @staticmethod
    def reserve_seat(screening_id, seat_number):
        connection = getCursor()
        update_query = """UPDATE screeningseat SET status='reserved' WHERE screeningID = %s AND seatNumber = %s"""
        connection.execute(update_query, (screening_id, seat_number))
    
    @staticmethod
    def delete_screeningseats(screening_id):
        try:
            connection = getCursor()
            delete_query = "DELETE FROM screeningseat WHERE screeningID = %s"
            connection.execute(delete_query, (screening_id,))
            return True
        except Exception as e:
            print(f"Error while deleting movie: {e}")
            return False

