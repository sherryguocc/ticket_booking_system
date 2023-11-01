import datetime
from APP import getCursor
import json
from datetime import timedelta

class Movie:
    """! @brief The Movie class"""
    def __init__(self, movieID: int, title: str, description:str, durationMins:int, language: str, releaseDate: datetime, country:str, genre:str, status:str):
        self.__movieID = movieID
        self.__title = title
        self.__description = description
        self.__durationMins = durationMins
        self.__language = language
        self.__releaseDate = releaseDate
        self.__country = country
        self.__genre = genre
        self.__status = status
    
    # Property getters and setters for various attributes.
    # These allow controlled access to the private attributes.
    
    @property
    def movieID (self):
        return self.__movieID
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def durationMins(self):
        return self.__durationMins

    @durationMins.setter
    def durationMins(self, durationMins):
        self.__durationMins = durationMins

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        self.__language = language

    @property
    def releaseDate(self):
        return self.__releaseDate

    @releaseDate.setter
    def releaseDate(self, releaseDate):
        self.__releaseDate = releaseDate

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @staticmethod
    def get_movie_list():
        connection = getCursor()
        movieListQuery = """SELECT * FROM movie WHERE status='showing'"""
        connection.execute(movieListQuery)
        rows = connection.fetchall()

        movie_list = []

        for row in rows:
            movie_id = row[0]
            movie_title = row[1]
            description = row[2]
            duration = row[3]
            language = row[4]
            release_date = row[5]
            country = row[6]
            genre = row[7]
            status = row[8]

            # Create a Movie object and append it to the list
            movie = Movie(
                movieID=movie_id,
                title=movie_title,
                description=description,
                durationMins=duration,
                language=language,
                releaseDate=release_date,
                country=country,
                genre=genre,
                status=status,
            )
            movie_list.append(movie)

        return movie_list

    @classmethod
    def search(cls, search_query):
        searched_movies = []
        connection = getCursor()
        search = """
            SELECT * FROM movie
            WHERE title LIKE %s OR 
            description LIKE %s OR
            description LIKE %s OR
            durationMins LIKE %s OR
            language LIKE %s OR
            releaseDate LIKE %s OR
            country LIKE %s OR
            genre LIKE %s
        """
        connection.execute(search, ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
        results = connection.fetchall()
        for row in results:
            movie = cls(
                movieID=row[0],
                title=row[1],
                description=row[2],
                durationMins=row[3],
                language=row[4],
                releaseDate=row[5],
                country=row[6],
                genre=row[7],
                status=row[8],
            )
            searched_movies.append(movie)
    
        return searched_movies

    @classmethod
    def add_movie(cls, movie):
        try:
            connection = getCursor()
            insert_query = """
                INSERT INTO movie (title, description, durationMins, language, releaseDate, country, genre, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (movie.title, movie.description, movie.durationMins, movie.language, movie.releaseDate, movie.country, movie.genre, movie.status)
            connection.execute(insert_query, values)
            movie_id = connection.lastrowid
            return movie_id
        except Exception as e:
            print(f"Error while adding a new movie: {e}")
            return None
    
    @staticmethod
    def get_movie_by_id(movieID):
        connection = getCursor()
        query = """ SELECT * FROM movie WHERE movieID = %s """
        connection.execute(query,(movieID,))
        result = connection.fetchone()
        if result:
            movie = Movie(
                    movieID=result[0],
                    title=result[1],
                    description=result[2],
                    durationMins=result[3],
                    language=result[4],
                    releaseDate=result[5],
                    country=result[6],
                    genre=result[7],
                    status=result[8],
                )
            return movie
            
        else:
            return False
        
    @staticmethod
    def delete_movie(movie_id):
        try:
            connection = getCursor()
            delete_query = "DELETE FROM movie WHERE movieID = %s"
            connection.execute(delete_query, (movie_id,))
            return True
        except Exception as e:
            print(f"Error while deleting movie: {e}")
            return False
    
    @staticmethod
    def cancel_movie(movie_id):
        try:
            connection = getCursor()
            update_query = "UPDATE movie SET status='cancelled' WHERE movieID = %s"
            connection.execute(update_query, (movie_id,))
            print("movie status updated")
            return True
        except Exception as e:
            print(f"Error while deleting movie: {e}")
            return False    

class Screening:
    def __init__(self, screeningID: int, movieID: int, date: datetime, startTime: datetime, endTime: datetime, hallID: int, price: float, status:str):
        self.__screeningID = screeningID
        self.__movieID = movieID
        self.__date = date
        self.__startTime = startTime
        self.__endTime = endTime
        self.__hallID = hallID
        self.__price = price
        self.__status = status
    
    # Property getters and setters for various attributes.
    # These allow controlled access to the private attributes.
    
    @property
    def screeningID (self):
        return self.__screeningID
    
    @property
    def movieID(self):
        return self.__movieID
    
    @movieID.setter
    def movieID(self, number):
        self.__movieID = number
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, new_date):
        self.__date = new_date
    
    @property
    def startTime(self):
        return self.__startTime
    
    @startTime.setter
    def startTime(self, new_start_time):
        self.__startTime = new_start_time
    
    @property
    def endTime(self):
        return self.__endTime
    
    @endTime.setter
    def endTime(self, new_end_time):
        self.__endTime = new_end_time

    @property
    def hallID(self):
        return self.__hallID
    
    @hallID.setter
    def hallID(self, new_hall_id):
        self.__hallID = new_hall_id

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    @staticmethod
    def get_screening_list(movie_id):
        connection = getCursor()
        query = "SELECT * FROM screening where movieID = %s and status='showing'"
        connection.execute(query, (movie_id,))
        rows = connection.fetchall()

        screening_list = []

        for row in rows:
            screening_id = row[0]
            date = row[2]
            start_time = row[3]
            end_time = row[4]
            hall_id = row[5]
            price = row[6]
            status = row[7]

            # Create a Screening object and append it to the list
            screening = Screening(
                screeningID=screening_id,
                movieID=movie_id,
                date=date,
                startTime=start_time,
                endTime=end_time,
                hallID=hall_id,
                price=price,
                status=status
            )
            screening_list.append(screening)

        return screening_list
    
    @classmethod
    def add_screening(cls, screening):
        try:
            connection = getCursor()
            insert_query = """
                INSERT INTO screening (movieID, date, startTime, endTime, hallID, price,status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            connection.execute(insert_query, (screening.movieID, screening.date, screening.startTime, screening.endTime, screening.hallID, screening.price, screening.status))
            screening_id = connection.lastrowid
            return screening_id
        except Exception as e:
            print("Error while adding screening:", e)
            return False
        
    @classmethod
    def is_hall_available(cls, hallID, date, start_time, end_time):
        connection = getCursor()
        query = """ SELECT * FROM screening WHERE hallID = %s and date = %s """
        connection.execute(query,(hallID,date))
        results = connection.fetchall()
        screenings = []
        for row in results:
            screening_start_time = datetime.datetime.strptime(str(row[3]), '%H:%M:%S')
            screening_end_time = datetime.datetime.strptime(str(row[4]), '%H:%M:%S')
            screenings.append({
                'start_time': screening_start_time,
                'end_time': screening_end_time
            })
        start_time = datetime.datetime.strptime(start_time, '%H:%M')
        end_time = datetime.datetime.strptime(end_time, '%H:%M')
        for screening in screenings:
            if (start_time <= screening['end_time'] and end_time >= screening['start_time']):
                return False

        return True
    
    @classmethod
    def get_screening_by_id(cls,screening_id):
        connection = getCursor()
        query = """ SELECT * FROM screening WHERE screeningID = %s"""
        connection.execute(query,(screening_id,))
        result = connection.fetchone()
        if result:
            screening = Screening(
                    screeningID=result[0],
                    movieID=result[1],
                    date=result[2],
                    startTime=result[3],
                    endTime=result[4],
                    hallID=result[5],
                    price=result[6],
                    status=result[7]
                )
            return screening
            
        else:
            return False

    @staticmethod
    def cancel_screening(screening_id):
        try:
            connection = getCursor()
            update_query = "UPDATE screening SET status='cancelled' WHERE screeningID = %s"
            connection.execute(update_query, (screening_id,))
            return True
        except Exception as e:
            print(f"Error while deleting movie: {e}")
            return False
    