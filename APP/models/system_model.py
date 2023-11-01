from APP import getCursor
from datetime import datetime
import json,random,string

class Booking:
    def __init__(self, bookingID: int, userID: int, numberOfSeat: int, bookingDate: datetime, screeningID: int, seatList: list, amount: float, paymentID: int, status:str):
        self.__bookingID = bookingID
        self.__userID = userID
        self.__numberOfSeat = numberOfSeat
        self.__bookingDate = bookingDate
        self.__screeningID = screeningID
        self.__seatList = seatList
        self.__amount = amount
        self.__paymentID = paymentID
        self.__status = status

    @property
    def bookingID(self):
        return self.__bookingID

    @property
    def userID(self):
        return self.__userID
    
    @userID.setter
    def userID(self, user_id):
        self.__userID = user_id

    @property
    def numberOfSeat(self):
        return self.__numberOfSeat
    
    @numberOfSeat.setter
    def numberOfSeat(self, number):
        self.__numberOfSeat = number

    @property
    def bookingDate(self):
        return self.__bookingDate
    
    @bookingDate.setter
    def bookingDate(self, date):
        self.__bookingDate = date

    @property
    def screeningID(self):
        return self.__screeningID
    
    @screeningID.setter
    def screeningID(self, number):
        self.__screeningID = number

    @property
    def seatList(self):
        return self.__seatList
    
    @seatList.setter
    def seatList(self, seat_list):
        self.__seatList = seat_list

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def paymentID(self):
        return self.__paymentID
    
    @paymentID.setter
    def paymentID(self, number):
        self.__paymentID = number
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value

    @classmethod
    def add_booking(cls, booking):
        try:
            connection = getCursor()  
            insert_query = """
                INSERT INTO booking (userID, numberOfSeat, bookingDate, screeningID, seatList, amount, paymentID,status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            connection.execute(insert_query, (booking.userID, booking.numberOfSeat, booking.bookingDate, booking.screeningID, booking.seatList, booking.amount, booking.paymentID, booking.status))
            return True
        except Exception as e:
            return False
    
    @staticmethod
    def get_booking_list(user_id):
        try:
            connection = getCursor()
            select_query = """
                SELECT * FROM booking
                WHERE userID = %s
            """
            connection.execute(select_query, (user_id,))
            rows = connection.fetchall()

            booking_list = []

            for row in rows:
                booking = Booking(
                    bookingID=row[0],
                    userID=row[1],
                    numberOfSeat=row[2],
                    bookingDate=row[3],
                    screeningID=row[4],
                    seatList=json.loads(row[5]),
                    amount=row[6],
                    paymentID=row[7],
                    status=row[8]
                )

                # Create a dictionary representing the booking
                booking_dict = {
                    'bookingID': booking.bookingID,
                    'userID': booking.userID,
                    'numberOfSeat': booking.numberOfSeat,
                    'bookingDate': booking.bookingDate,
                    'screeningID': booking.screeningID,
                    'seatList': booking.seatList,
                    'amount': booking.amount,
                    'paymentID': booking.paymentID,
                    'status': booking.status
                }

                booking_list.append(booking_dict)
            return booking_list
        except Exception as e:
            return []
        
    @staticmethod
    def cancel_booking(booking_id):
        try:
            connection = getCursor() 
            update_query = "UPDATE booking SET status = 'cancelled' WHERE bookingID = %s"
            connection.execute(update_query, (booking_id,))
            return True
        except Exception as e:
            return False

    @classmethod
    def find_booking_by_id(cls, booking_id):
        try:
            connection = getCursor() 
            query = "SELECT * FROM booking WHERE bookingID = %s"
            connection.execute(query, (booking_id,))
            booking_data = connection.fetchone()
            if booking_data:
                booking = cls(
                    bookingID=booking_data[0],
                    userID=booking_data[1],
                    numberOfSeat=booking_data[2],
                    bookingDate=booking_data[3],
                    screeningID=booking_data[4],
                    seatList=json.loads(booking_data[5]),
                    amount=booking_data[6],
                    paymentID=booking_data[7],
                    status=booking_data[8]
                )
                return booking
            else:
                return None
        except Exception as e:
            return None
    
    @staticmethod
    def update_paid_booking(booking_id, payment_id):
        try:
            connection = getCursor()
            query = "UPDATE booking SET paymentID = %s, status = %s WHERE bookingID = %s"
            connection.execute(query, (payment_id, "paid", booking_id))
            return True
        except Exception as e:
            return False
    
    @staticmethod
    def find_booking_ids_by_screening_id(screening_id):
        connection = getCursor()
        query = "SELECT bookingID FROM booking WHERE screeningID = %s;"
        connection.execute(query, (screening_id,))
        booking_ids = {row[0] for row in connection.fetchall()}
        return booking_ids
    
    @staticmethod
    def find_booking_ids_by_movie_id(screening_id):
        connection = getCursor()
        query = "SELECT bookingID FROM booking WHERE screeningID = %s;"
        connection.execute(query, (screening_id,))
        booking_ids = {row[0] for row in connection.fetchall()}
        return booking_ids
    
    @staticmethod
    def find_user_ids_by_booking_id(booking_id):
        connection = getCursor()
        query = "SELECT userID FROM booking WHERE screeningID = %s;"
        connection.execute(query, (booking_id,))
        user_ids = {row[0] for row in connection.fetchall()}
        return user_ids

  
class Coupon:
    def __init__(self, couponID: int,expiryDate:datetime, discount: float, couponCode:str):
        self.__couponID = couponID
        self.__expiryDate = expiryDate
        self.__discount = discount
        self.__couponCode = couponCode

    @property
    def couponID(self):
        return self.__couponID

    @couponID.setter
    def couponID(self, couponID):
        self.__couponID = couponID

    @property
    def expiryDate(self):
        return self.__expiryDate

    @expiryDate.setter
    def expiryDate(self, expiryDate):
        self.__expiryDate = expiryDate

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount = discount

    @property
    def couponCode(self):
        return self.__couponCode

    @couponCode.setter
    def couponCode(self, couponCode):
        self.__couponCode = couponCode

    @staticmethod
    def get_coupon_list():
        connection = getCursor()
        connection.execute("""SELECT * FROM coupon""")
        rows = connection.fetchall()

        coupon_list = []

        for row in rows:
            couponID = row[0]
            expiryDate = row[1]
            discount = row[2]
            couponCode = row[3]

            # Create a Coupon object and append it to the list
            coupon = Coupon(
                couponID = couponID,
                expiryDate =  expiryDate,
                discount = discount,
                couponCode = couponCode
                )
            coupon_list.append(coupon)
            print("coupon_list",coupon_list)
        return coupon_list

    @classmethod
    def add_coupon(cls, coupon):
        try:
            connection = getCursor()
            # Generate a unique 4-character coupon code
            while True:
                coupon_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
                print("first coupon_code:",coupon_code)
                check_query = "SELECT * FROM coupon WHERE couponCode = %s"
                connection.execute(check_query, (coupon_code,))
                result=connection.fetchone()
                if not result:
                    break
            print("coupon_code create:",coupon_code)
            insert_query = """
                INSERT INTO coupon (expiryDate, discount, couponCode)
                VALUES (%s, %s, %s)
            """
            print("Inserting new coupon:", coupon)
            values = (coupon.expiryDate, coupon.discount, coupon_code)
            connection.execute(insert_query, values)
            coupon_id = connection.lastrowid
            if coupon_id: 
                print("insert new coupon succeed")
                print("Inserted coupon ID:", coupon_id)
                return coupon_id
        except Exception as e:
            return None
        
    def get_id_by_code(code):
        connection = getCursor()
        query = """SELECT couponID FROM coupon WHERE couponCode = %s"""
        connection.execute(query, (code,))
        result = connection.fetchone()
        if result:
            coupon_id=result[0]
            print("coupon_id",coupon_id)
            return coupon_id
        return None
        
    def get_discount_by_code(code):
        connection = getCursor()
        discount_query = "SELECT * FROM coupon WHERE couponCode = %s"
        connection.execute(discount_query, (code,))
        result = connection.fetchone()
        if result:
            discount = result[2]
            expiry_date = result[1]
            current_date = datetime.now().date() 
            if current_date <= expiry_date:
                return discount
            else:
                return None
        else:
            return None
    
class Payment:
    def __init__(self, paymentID: int, amount: float, date: datetime, couponID: int, creditCardID:int, debitCardID:int, status: str):
        self.__paymentID = paymentID
        self.__amount = amount
        self.__date = date
        self.__couponID = couponID
        self.__creditCardID = creditCardID
        self.__debitCardID = debitCardID
        self.__status = status

    @property
    def paymentID(self):
        return self.__paymentID

    @paymentID.setter
    def paymentID(self, paymentID):
        self.__paymentID = paymentID

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def couponID(self):
        return self.__couponID

    @couponID.setter
    def couponID(self, couponID):
        self.__couponID = couponID

    @property
    def creditCardID(self):
        return self.__creditCardID

    @creditCardID.setter
    def creditCardID(self, creditCardID):
        self.__creditCardID = creditCardID

    @property
    def debitCardID(self):
        return self.__debitCardID

    @debitCardID.setter
    def debitCardID(self, debitCardID):
        self.__debitCardID = debitCardID
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @classmethod
    def add_payment(cls, payment):
        try:
            connection = getCursor()
            insert_query = """
                INSERT INTO payment (amount, date, couponID, creditCardID, debitCardID, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            connection.execute(insert_query, (payment.amount, payment.date, payment.couponID, payment.creditCardID, payment.debitCardID, payment.status))
            payment_id = connection.lastrowid
            print("payment id in model:", payment_id)
            return payment_id
        except Exception as e:
            print('add payment error')
            return False
    
    @staticmethod
    def cancel_and_refund(payment_id):
        try:
            connection = getCursor()
            update_query = "UPDATE payment SET status = %s WHERE paymentID = %s"
            connection.execute(update_query, ('refund', payment_id))
            return True
        except Exception as e:
            return False
    
    @staticmethod
    def get_payment_by_id(payment_id):
        connection = getCursor()
        query = "SELECT * from payment WHERE paymentID = %s"
        connection.execute(query, (payment_id,))
        result = connection.fetchone()
        if result:
            return result
        else:
            return False

class CreditCard:
    def __init__(self, creditcardID,cardNumber,cardType,expiryDate,nameOnCard,securityNumber):
        self.__creditcardID = creditcardID
        self.__cardNumber = cardNumber
        self.__cardType = cardType
        self.__expiryDate = expiryDate
        self.__nameOnCard = nameOnCard
        self.__securityNumber = securityNumber

    @property
    def creditcardID(self):
        return self.__creditcardID

    @property
    def cardNumber(self):
        return self.__cardNumber

    @cardNumber.setter
    def cardNumber(self, number):
        self.__cardNumber = number

    @property
    def cardType(self):
        return self.__cardType

    @cardType.setter
    def cardType(self, card_type):
        self.__cardType = card_type

    @property
    def expiryDate(self):
        return self.__expiryDate

    @expiryDate.setter
    def expiryDate(self, expiry_date):
        self.__expiryDate = expiry_date

    @property
    def nameOnCard(self):
        return self.__nameOnCard

    @nameOnCard.setter
    def nameOnCard(self, name):
        self.__nameOnCard = name

    @property
    def securityNumber(self):
        return self.__securityNumber

    @securityNumber.setter
    def securityNumber(self, security_number):
        self.__securityNumber = security_number

    @classmethod
    def add_creditcard(cls, creditcard):
        connection = getCursor()
        insert_query = """
            INSERT INTO creditcard (cardNumber, cardType, expiryDate, nameOnCard, securityNumber)
            VALUES (%s, %s, %s, %s, %s)
        """
        connection.execute(insert_query, (creditcard.cardNumber, creditcard.cardType, creditcard.expiryDate, creditcard.nameOnCard, creditcard.securityNumber))
        creditcard_id = connection.lastrowid
        if creditcard_id:
            return creditcard_id
        else: 
            print("No creditcard_id found")

class CashPayment(Payment):
    """! 
    @brief Derived class that inherits from Payment.
    @sa Payment
    """
    def __init__(self, paymentID: int, customerID: int, amount: float, paymentDate: datetime):
        """! Create a Cash Payment object.
        @param paymentID The unique payment identifier.
        @param customerID The identifier of the customer making the payment.
        @param amount The payment amount.
        @param paymentDate The date and time of the payment.
        """
        super().__init__(paymentID, customerID, amount, paymentDate, "Cash")

    def get_cash_payment(self):
        """! Getter and Setter methods for CashPayment attributes
        """
        return self._cash_payment

    def set_cash_payment(self, cash_payment):
        """! Getter and Setter methods for CashPayment attributes
        """
        self._cash_payment = cash_payment

    def __str__(self):
        """! Return a string representation of the CashPayment object.
        """
        return f"Cash Payment Information:\nPayment ID: {self._paymentID}\nCustomer ID: {self._customerID}\nAmount: {self._amount}\nPayment Date: {self._paymentDate}"

class DebitCard():
    def __init__(self, debitcardID, cardNumber, bankName, nameOnCard):
        self.__debitcardID = debitcardID
        self.__cardNumber = cardNumber
        self.__bankName = bankName
        self.__nameOnCard = nameOnCard
    
    @property
    def debitcardID(self):
        return self.__debitcardID

    @property
    def cardNumber(self):
        return self.__cardNumber

    @cardNumber.setter
    def cardNumber(self, number):
        self.__cardNumber = number

    @property
    def bankName(self):
        return self.__bankName

    @bankName.setter
    def bankName(self, bank_name):
        self.__bankName = bank_name

    @property
    def nameOnCard(self):
        return self.__nameOnCard

    @nameOnCard.setter
    def nameOnCard(self, name):
        self.__nameOnCard = name
    
    @classmethod
    def add_debitcard(cls, debittcard):
        connection = getCursor()
        insert_query = """
            INSERT INTO debitcard (cardNumber, bankName, nameOnCard)
            VALUES (%s, %s, %s)
        """
        connection.execute(insert_query, (debittcard.cardNumber, debittcard.bankName, debittcard.nameOnCard))
        debittcard_id = connection.lastrowid
        if debittcard_id:
            return debittcard_id
        else: 
            print("No creditcard_id found")

class Notification():
    def __init__(self, notificationID, date, content, userID):
        self.__notificationID = notificationID
        self.__date = date
        self.__content = content
        self.__userID = userID
    
    @property
    def debitcardID(self):
        return self.__notificationID

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, userID):
        self.__userID = userID

    @staticmethod
    def get_notification_list(user_id):
        connection = getCursor()
        query="""SELECT * FROM notification WHERE userID = %s"""
        connection.execute(query, (user_id,))
        rows = connection.fetchall()

        notification_list = []

        for row in rows:
            notificationID = row[0]
            date = row[1]
            content = row[2]
            userID = row[3]

            # Create a notification object and append it to the list
            notification = Notification(
                notificationID = notificationID,
                date =  date,
                content = content,
                userID = userID
                )
            notification_list.append(notification)
            print("notification_list",notification_list)
        return notification_list
    
    @staticmethod
    def send_booking_notes(user_id):
        content = "You have successfully booked a screening. Please view your booking list to pay."
        date=datetime.now()
        connection=getCursor()
        insert_query = """
                INSERT INTO notification (date, content, userID)
                VALUES (%s, %s, %s)
            """
        values = (date, content, user_id)
        connection.execute(insert_query, values)
        note_id = connection.lastrowid
        if note_id:
            return note_id
        else:
            return None
    
    @staticmethod
    def send_payment_notes(user_id):
        content = "You have successfully made a payment. Please view your booking list to check."
        date = datetime.now()
        connection = getCursor()
        insert_query = """
                INSERT INTO notification (date, content, userID)
                VALUES (%s, %s, %s)
            """
        values = (date, content, user_id)
        connection.execute(insert_query, values)
        note_id = connection.lastrowid
        if note_id:
            return note_id
        else:
            return None
        
    @staticmethod
    def send_cancel_notes_without_pay(user_id):
        content = "Your booking has been cancelled. Please view your booking list to check."
        date = datetime.now()
        connection = getCursor()
        insert_query = """
                INSERT INTO notification (date, content, userID)
                VALUES (%s, %s, %s)
            """
        values = (date, content, user_id)
        connection.execute(insert_query, values)
        note_id = connection.lastrowid
        if note_id:
            return note_id
        else:
            return None
        
    @staticmethod
    def send_cancel_notes_with_pay(user_id):
        content = "Your booking has been cancelled. We will refund the payment amount to your account."
        date = datetime.now()
        connection = getCursor()
        insert_query = """
                INSERT INTO notification (date, content, userID)
                VALUES (%s, %s, %s)
            """
        values = (date, content, user_id)
        connection.execute(insert_query, values)
        note_id = connection.lastrowid
        if note_id:
            return note_id
        else:
            return None
        
    @staticmethod
    def screening_cancel_notes(user_id):
        content = "Sorry to inform you that, the screening you booked has been cancelled.If you have paid, we will make refund to your account. "
        date = datetime.now()
        connection = getCursor()
        insert_query = """
                INSERT INTO notification (date, content, userID)
                VALUES (%s, %s, %s)
            """
        values = (date, content, user_id)
        connection.execute(insert_query, values)
        note_id = connection.lastrowid
        if note_id:
            return note_id
        else:
            return None
        
    @staticmethod
    def movie_cancel_notes(user_id):
        content = "Sorry to inform you that, the movie you booked has been cancelled. If you have paid, we will make refund to your account."
        date = datetime.now()
        connection = getCursor()
        insert_query = """
                INSERT INTO notification (date, content, userID)
                VALUES (%s, %s, %s)
            """
        values = (date, content, user_id)
        connection.execute(insert_query, values)
        note_id = connection.lastrowid
        if note_id:
            return note_id
        else:
            return None
