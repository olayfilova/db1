import sqlite3
import pandas as pd



conn = sqlite3.connect('../INSTRUCTOR.db')
cursor_obj = conn.cursor()

cursor_obj.execute('DROP TABLE IF EXISTS INSTRUCTOR')

table = "create table if not exists INSTRUCTOR (ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2)); "
cursor_obj.execute(table)
print("Table is ready")

cursor_obj.execute('insert into INSTRUCTOR VALUES(1, "RAV", "ASHUJA", "TORONTO", "CA")')
cursor_obj.execute('insert into INSTRUCTOR VALUES(2, "RAUL", "CHONG", "MARKHAM", "CA"), (3, "PHILL", "MCCONNOR", "CHICAGO", "US")')

statement = 'select * from INSTRUCTOR'
cursor_obj.execute(statement)
print( 'All the Data')

output_all = cursor_obj.fetchall()
for row_all in output_all:
    print(row_all)

statement = "select * from INSTRUCTOR"
cursor_obj.execute(statement)
print('all the Data')

output_many= cursor_obj.fetchmany(2)
for row_many in output_many:
    print(row_many)

statement = "select FNAME FROM INSTRUCTOR"
cursor_obj.execute(statement)
print("All the Data")

output_col = cursor_obj.fetchall()
for i in output_col:
    print(i)

query_upd = "update INSTRUCTOR SET CITY = 'MOOSETOWN' WHERE FNAME = 'RAV'"
cursor_obj.execute(query_upd)


statement  = "select * from INSTRUCTOR"
cursor_obj.execute(statement)
print("All the data")

output1 = cursor_obj.fetchall()
for i in output1:
    print(i)

import pandas as pd
df = pd.read_sql_query('select * from INSTRUCTOR;', conn)
print(df)
print(df.LNAME[0])
print(df.shape)

conn.close()








