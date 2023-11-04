# cinema
COMP642 individual assignment

how to run this webapp:
1. run mySQL scrpit: cinemadb.sql
2. cmd: python app.py
3. open http://127.0.0.1:5000/ in browser


Users account:
Admin account:
username : admin1
password : 123456

Staff account:
username : staff1
password : 123456

Customer account:
username : customer1
password ：123456

About test:
Because most of my methods have queries that call the database, I tried various methods to avoid calling the original database in the test, including establishing a test database and connecting the test code to the test database. However, since the getCursor method used is a global connection method, during the test, calling the method under test has to connect to the original database, so I gave up this method.
The mock connection method finally adopted forces a return result to the method, so the test can pass smoothly, but I don't understand the meaning of using the return result I arranged to match the test result I want. So I didn't write all the tests this way because I couldn't accept test results that I didn't understand. Regarding testing, I am still learning.
