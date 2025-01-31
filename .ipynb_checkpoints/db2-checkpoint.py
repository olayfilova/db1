import random
import sqlite3
import os
import pandas as pd
import string
from string import ascii_lowercase
from utils_dir.function import reading_text_file_readlines
import sqlalchemy
import csv



# conn = sqlite3.connect('../INSTRUCTOR.db')
# cursor_obj = conn.cursor()
# #
# # cursor_obj.execute('DROP TABLE IF EXISTS INSTRUCTOR')
#
# # table = "create table if not exists INSTRUCTOR (ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2)); "
# # cursor_obj.execute(table)
# # print("Table is ready")
# #
# cursor_obj.execute('insert into INSTRUCTOR VALUES(1, "RAV", "ASHUJA", "TORONTO", "CA")')
# cursor_obj.execute('insert into INSTRUCTOR VALUES(2, "RAUL", "CHONG", "MARKHAM", "CA"), (3, "PHILL", "MCCONNOR", "CHICAGO", "US")')
#
# # statement = 'select * from INSTRUCTOR'
# # cursor_obj.execute(statement)
# # print( 'All the Data')
# #
# # output_all = cursor_obj.fetchall()
# # for row_all in output_all:
# #     print(row_all)
#
# # statement = "select * from INSTRUCTOR"
# # cursor_obj.execute(statement)
# # print('all the Data')
# # cursor_obj.close()
#
# # output_many= cursor_obj.fetchmany(2)
# # for row_many in output_many:
# #     print(row_many)
# #
# # statement = "select FNAME FROM INSTRUCTOR"
# # cursor_obj.execute(statement)
# # print("All the Data")
# #
# # output_col = cursor_obj.fetchall()
# # for i in output_col:
# #     print(i)
# #
# # query_upd = "update INSTRUCTOR SET CITY = 'MOOSETOWN' WHERE FNAME = 'RAV'"
# # cursor_obj.execute(query_upd)
# #
# #
# # statement = "select * from INSTRUCTOR"
# # cursor_obj.execute(statement)
# # print("All the data")
# #
# # output1 = cursor_obj.fetchall()
# # for i in output1:
# #     print(i)
# #
# #
# # df = pd.read_sql_query('select * from INSTRUCTOR;', conn)
# # print(df)
# # print(df.LNAME[0])
# # print(df.shape)
# #
# # conn.close()
# #
# # #
# #
# # import sqlite3
# #
#
# # conn = sqlite3.connect('INSTRUCTOR.db')
# # cursor_obj = conn.cursor()
# cursor_obj.execute('insert into INSTRUCTOR VALUES(10, "Maria", "Fernando", "Dublin", "IR")')
# #
# # print("3")
# #
# # statement = "select * from INSTRUCTOR2"
# # curs_obj.execute(statement)
# # output = curs_obj.fetchall()
# # for i in output:
# #     print(i)
# #
# #
# # curs_obj.close()
#
# # import sqlite3
#
#
# # conn = sqlite3.connect('../INSTRUCTOR.db')
# #
# # cursor_obj = conn.cursor()
# cursor_obj.execute("insert into INSTRUCTOR VALUES(4, 'PAUL', 'Marko', 'San-Paulo', 'BR')")
# #
# statement2 = 'select * from INSTRUCTOR'
# cursor_obj.execute(statement2)
# output = cursor_obj.fetchall()
# for i in output:
#     print(i)
#
# cursor_obj.close()

# conn = sqlite3.connect('../INSTRUCTOR2.db')
# curs_obj = conn.cursor()
# # curs_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR2")
# # table = 'create table IF NOT EXISTS INSTRUCTOR2(ID INTEGER PRIMARY KEY NOT NULL, F_NAME VARCHAR(20), S_NAME VARCHAR(20), CITY VARCHAR(20), CCODE VARCHAR(2))'
# # curs_obj.execute(table)
# print("2")
#
# statement = 'insert into INSTRUCTOR2 VALUES(31, "ORELINE", "HADDAD", "Damascus", "SY")'
# curs_obj.execute(statement)
# output = curs_obj.fetchall()
# for i in output:
#     print(i)
#
# curs_obj.execute('insert into INSTRUCTOR2 VALUES(33, "ORELINE", "HADDAD", "Damascus", "SY")')
# statement = 'select * from INSTRUCTOR2'
# curs_obj.execute(statement)
# output = curs_obj.fetchall()
# # for i in output:
# #     print(i)
#
# curs_obj.execute('update INSTRUCTOR2 set f_name = "Clara" ,s_name = "Wargghm" where id= 33')
# statement = 'select * from INSTRUCTOR2'
# curs_obj.execute(statement)
# output = curs_obj.fetchall()
# for i in output:
#     print(i)
#
# curs_obj.execute('update INSTRUCTOR2 set city="Madrid", ccode = "SP" where id = 33')
# curs_obj.execute('select * from INSTRUCTOR2')
# output = curs_obj.fetchall()
# for i in output:
#     print(i)
#
# df = pd.read_sql_query("select * from INSTRUCTOR2", conn)
# print(df)
# print(f'{df.F_NAME[0]} and {df.F_NAME[1]}')
# print(df.S_NAME[0])
# conn.close()
#
# # file_name ='../Macintosh HD/data/Users/olgafilova/Downloads/sakila-db'
#
#
# # data = reading_text_file_readlines(file=file_name)
# # print(data)

# #######################
# import os
# from utils_dir.function import reading_text_file_readlines
#
# data = reading_text_file_readlines("../db1/sakila-db/sakila-data.sql")
# print(data)
#
# filename = "db1"
# file_list = os.listdir("../db1")
# print(file_list)
#
# for file in file_list:
#     if os.path.isfile(file):
#         print(file)
#
# file_name = ""
# file_dir = ""
# some_dir = ""
# # data = reading_text_file_readlines(f"{file_dir}/{file_name}")
# data = reading_text_file_readlines("../db1/sakila-db/sakila-data.sql")
# # data = reading_text_file_readlines(os.path.join(file_dir, file_name))
# print(data)


# ###############################################################################
# def create_dir(name):
#     os.makedirs(name, exist_ok=True)
#
#
# def create_file(sym, some_dir, ascii_lowercase):
#     text = ascii_lowercase.replace(sym, sym.upper())
#     full_path = os.path.join(some_dir, sym)
#     with open(full_path + ".txt", "w") as f:
#         f.write(text)
#
#
# def create_files(dir, ascii_lowercase):
#     for symb in ascii_lowercase:
#         create_file(symb, dir, ascii_lowercase)
#
#
# def remove_half_of_files(dir_name):
#     files_list = os.listdir(dir_name)
#     random.shuffle(files_list)
#     file_to_delete = files_list[:len(files_list) // 2]
#     for to_del in file_to_delete:
#         os.remove(os.path.join(dir_name, to_del))
#
#
# dir_name = "alPHa"
#
# create_directory = create_dir(dir_name)
# create_files(dir_name, ascii_lowercase)
# remove_half_of_files(dir_name)
#
#
#

#
#
# ###########################
# ###########################
import sqlite3

# def connect_to_db(db_name):
#     """Connect to the SQLite database."""
#     try:
#         conn = sqlite3.connect(db_name)
#         print("Connection successful")
#         return conn
#     except sqlite3.Error as e:
#         print(f"Error connecting to database: {e}")
#         return None
#
# def fetch_data(conn, query):
#     """Fetch data from the database."""
#     try:
#         cursor = conn.cursor()
#         cursor.execute(query)
#         rows = cursor.fetchall()
#         return rows
#     except sqlite3.Error as e:
#         print(f"Error fetching data: {e}")
#         return []
#
# # def main():
# #     db_name = 'sakila.db'
# #     conn = connect_to_db(db_name)
# #
# #     if conn:
# #         query = "SELECT first_name, last_name FROM actor LIMIT 10;"
# #         results = fetch_data(conn, query)
# #         for row in results:
# #             print(row)
# #
# #         conn.close()
# #
# # if __name__ == "__main__":
# #     main()
#
#
# connect_to_db('sakila-data.sql')

# data = reading_text_file_readlines("../db1/sakila-db/sakila-data.sql")
# with open("../db1/sakila-db/sakila-schema.sql", 'r') as f:
#     data = f.readlines()
# print(data[0])

conn = sqlite3.connect('postgres')
curs_obj = conn.cursor()
curs_obj.execute("DROP TABLE IF EXISTS weather")
table = "CREATE TABLE IF NOT EXISTS weather (city varchar(80), temp_lo int, temp_hi int,\
         prcp real --precipitation, date date); "
curs_obj.execute(table)

curs_obj.execute('insert into weather VALUES("San Francisco", 46, 50 , 0.25, "1991-11-27")')

table2 = ('create table cities(name varchar (80),\
        location point);')
curs_obj.execute(table2)
curs_obj.execute('INSERT INTO  cities VALUES("San Francisco", -194.0, 53.0 )')


statement1= curs_obj.execute("select * from weather")
output = statement1.fetchall()
for i in output:
    print(i)

# import csv
#
# filename = "sakila-db/sakila-schema.sql"
#
#
# def read_csv_file(name):
#     data = []
#     with open(name, 'r') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             data.append(row)
#     return data
#
#
# print(read_csv_file(filename))


# def write_csv_file(name, data):
#     with open(name, 'w') as f:
#         writer = csv.writer(f)
#         writer.writerows(data)
#
# data = read_csv_file(filename)
# print(data)

# header = data.pop(27)
# print(header)
# print(data)

# for row in data:


def read_csv_file_dict(name):
    data = []
    with open(name, 'r') as f:
        reader = csv.DictReader(f) #fieldnames=data[0].keys())
        for row in reader:
            data.append(row)
    return data


data = read_csv_file_dict(filename)
print(data)

# conn = sqlite3.connect("../sakila.db.sql")
# df =pd.read_sql("sakila-schema.sql", conn)
# df.to_sql('sakila-data.sql', conn, if_exists='replace', index =False, method = 'multi')
# # print(df.head())
# #
# curs_obj = conn.cursor()
# # #
# curs_obj.execute('USE sakila;')
# output = curs_obj.fetchall()
# for i in output:
#     table_names = i[0]
#     print(table_names)


import sqlite3
#
#
# def list_tables('../db1/sakila-db/sakila-data.sql': str):
#     # Connect to the SQLite database
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#
#     # Execute the query to retrieve all table names
#     cursor.execute("SELECT * FROM sqlite_master ;")
#
#     # Fetch all results
#     tables = cursor.fetchall()
#
#     # Close the connection
#     conn.close()
#
#     # Print the table names
#     print("Tables in the database:")
#     for table in tables:
#         print(table[0])
#
#
#
# db_path = '../sakila-db.tar.gz'
# list_tables(db_path)
#
