import pandas as pd
import logging
from datetime import datetime, timedelta
from mysql.connector import connect, Error
import mysql

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("practice.log")
ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
console_handler.setFormatter(ch_formatter)
file_handler.setFormatter(fh_formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)



# error handling to database from CSV and using functions
data = pd.read_csv (r'C:\Jeremy_code\CSV_To_Database\csvtodb.csv')   
df = pd.DataFrame(data)
row= None

def insertdb(row): #functions
    try:
        mydb = mysql.connector.connect(
            host="192.168.1.55",
            user="zijiang.tee",
            password="!nttsg2021",
            database="zijiang.tee"
            )

        my_cursor = mydb.cursor()


        for row in df.itertuples():
            my_cursor.execute('''
                    INSERT INTO Practice(FirstName, LastName, Email, Phone, Address, City, State, Zip, Age)
                    VALUES (%s ,%s ,%s, %s ,%s ,%s, %s ,%s ,%s)
                    ''',
                    (row.FirstName,
                    row.LastName,
                    row.Email,
                    row.Phone,
                    row.Address,
                    row.City,
                    row.State,
                    row.Zip,
                    row.Age)
                    )
        
    except Error:
        print("error")
        logger.error("Unable to insert data", exc_info=True)
    finally:
        mydb.commit()

insertdb(row) #calling out the functions


# working codes

# mydb = mysql.connector.connect(
#     host="192.168.1.55",
#     user="zijiang.tee",
#     password="!nttsg2021",
#     database="zijiang.tee"
#     )

# my_cursor = mydb.cursor()


# sqlstuff = "INSERT INTO Practice(FirstName, LastName, Email, Phone, Address, City, State, Zip, Age) VALUES (%s ,%s ,%s, %s ,%s ,%s, %s ,%s ,%s)"
# record1 = ("He", "she", "HEHO.com", 1234567, "SG", "SG", "SG", 123456, 12)

# my_cursor.execute(sqlstuff,record1)
# mydb.commit()

# first = "hee"
# last ="she"
# email = "hello.com"
# tele = 12345678999
# country = "SG"
# city = "SG"
# state = "SG"
# zip = 12345678999
# age = 15

# #record1 = ("He", "she", "HEHE.com", 1234567, "SG", "SG", "SG", 123456, 13)

# def insert_insight(first, last, email, tele, country, city, state, zip, age):
#     try:
#         with connect(
#                 host="dutabot.com",
#                 user="zijiang.tee",
#                 password="!nttsg2021",
#                 database="zijiang.tee",
#         ) as connection:
#             q = """INSERT INTO `zijiang.tee`.Practice (FirstName, LastName, Email, Phone, Address, City, State, Zip, Age
#              ) VALUES %s ,%s ,%s, %s ,%s ,%s, %s ,%s ,%s) """

#             with connection.cursor() as cursor:
#                 #record1 = (first, last, email, tele, country, city, state, zip, age)
#                 cursor.execute(q, (first, last, email, tele, country, city, state, zip, age))
#                 #logger.info(f"{cursor.rowcount} rows inserted into Practice")
#                 connection.commit()
#     except Error:
#         print("error")
#         #logger.error("Unable to insert data", exc_info=True)
#     finally:
#         cursor.close()
#         connection.close()

# insert_insight(first, last, email, tele, country, city, state, zip, age)

# try:
#     with connect(
#             host="dutabot.com",
#             user="zijiang.tee",
#             password="!nttsg2021",
#             database="zijiang.tee",
#     ) as connection:
#         q = """INSERT INTO `zijiang.tee`.Practice (FirstName, LastName, Email, Phone, Address, City, State, Zip, Age
#          ) VALUES %s ,%s ,%s, %s ,%s ,%s, %s ,%s ,%s) """

#         with connection.cursor() as cursor:
#             record1 = ("World", "Hello", "HEllo.com", 1234567, "NY", "NY", "NY", 34333456, 50)
#             cursor.execute(q, record1)
#             #logger.info(f"{cursor.rowcount} rows inserted into Practice")
#             connection.commit()
# except Error:
#     logger.error("Unable to insert data", exc_info=True)
# finally:
#     cursor.close()
#     connection.close()

# #insert_insight(record1, q)



# #Code to insert data into CSV
# data = pd.read_csv (r'C:\Jeremy_code\CSV_To_Database\csvtodb.csv')   
# df = pd.DataFrame(data)

# print(df)

# mydb = mysql.connector.connect(
#     host="192.168.1.55",
#     user="zijiang.tee",
#     password="!nttsg2021",
#     database="zijiang.tee"
#     )

# my_cursor = mydb.cursor()


# for row in df.itertuples():
#     my_cursor.execute('''
#                 INSERT INTO Practice(FirstName, LastName, Email, Phone, Address, City, State, Zip, Age)
#                 VALUES (%s ,%s ,%s, %s ,%s ,%s, %s ,%s ,%s)
#                 ''',
#                 (row.FirstName,
#                 row.LastName,
#                 row.Email,
#                 row.Phone,
#                 row.Address,
#                 row.City,
#                 row.State,
#                 row.Zip,
#                 row.Age)
#                 )
# mydb.commit()



# # error handling to database
# data = pd.read_csv (r'C:\Jeremy_code\CSV_To_Database\csvtodb.csv')   
# df = pd.DataFrame(data)

# try:
#     mydb = mysql.connector.connect(
#         host="192.168.1.55",
#         user="zijiang.tee",
#         password="!nttsg2021",
#         database="zijiang.tee"
#         )

#     my_cursor = mydb.cursor()


#     for row in df.itertuples():
#         my_cursor.execute('''
#                 INSERT INTO Practice(FirstName, LastName, Email, Phone, Address, City, State, Zip, Age)
#                 VALUES (%s ,%s ,%s, %s ,%s ,%s, %s ,%s ,%s)
#                 ''',
#                 (row.FirstName,
#                 row.LastName,
#                 row.Email,
#                 row.Phone,
#                 row.Address,
#                 row.City,
#                 row.State,
#                 row.Zip,
#                 row.Age)
#                 )
    
# except Error:
#     print("error")
#     logger.error("Unable to insert data", exc_info=True)
# finally:
#     mydb.commit()


#     my_cursor.execute('''
#                 INSERT INTO Practice(FirstName, LastName, Email, Phone, Address, City, State, Zip, Age)
#                 VALUES (%s ,%s ,%s, %s ,%s ,%s, %s ,%s ,%s)
#                 ''',
#                 (row.FirstName,
#                 row.LastName,
#                 row.Email,
#                 row.Phone,
#                 row.Address,
#                 row.City,
#                 row.State,
#                 row.Zip,
#                 row.Age)
#                 )
# mydb.commit()


