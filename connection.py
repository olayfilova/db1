import ibm_db_sa
import sqlalchemy
import warnings
import pandas
from sqlalchemy import create_engine
# from sqlalchemy import create_engine, MetaData, Table
import pandas as pd
import sqlite3



# # Database connection string
# conn_str = "ibm_db_sa://_:_:_/bludb"
#
# # Create an SQLAlchemy engine
# engine = create_engine(conn_str)
#
# # Test the connection
# try:
#     with engine.connect() as connection:
#         # Execute a test query
#         result = connection.execute("SELECT 1 FROM SYSIBM.SYSDUMMY1")
#         for row in result:
#             print(row)
#
#         # Now let's say you want to reflect a table and query data
#         metadata = MetaData()
#         test_table = Table('YOUR_TABLE_NAME', metadata, autoload_with=engine)
#
#         # Query the table
#         query = test_table.select()
#         result = connection.execute(query)
#
#         for row in result:
#             print(row)
# except Exception as e:
#     print(f"An error occurred: {e}")


# from sqlalchemy import create_engine
#
# # Define connection string
# conn_str = 'ibm_db_sa://_:_:_/BLUDB'
#
# # Create engine
# engine = create_engine(conn_str)
# # Connect to the database
# with engine.connect() as connection:
#     result = connection.execute('SELECT * FROM your_table LIMIT 10')
#     for row in result:
#         print(row)
# print(conn_str)



# dsn_hostname = "_"
# dsn_uid = "_"
# dsn_pwd = "_"
#
# dsn_driver = "{IBM DB2 ODBC DRIVER}"
# dsn_database = "/bludb"
# dsn_port = "_"
# dsn_protocol = "TCPIP"
# dsn_security = "SSL"
#
#
# dsn = (
#     "DRIVER={0};"
#     "DATABASE={1};"
#     "HOSTNAME={2};"
#     "PORT={3};"
#     "PROTOCOL={4};"
#     "UID={5};"
#     "PWD={6};"
#     "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)
#
#
# try:
#     conn = ibm_db.connect(dsn, "", "")
#     print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
#
# except:
#     print ("Unable to connect: ", ibm_db.conn_errormsg() )
#
# print(dsn)
# ibm_db.close(conn)



#
# conn_str = 'ibm_db_sa://_:_:_/BLUDB'
#
#
# engine = create_engine(conn_str)
#
#
# with engine.connect() as connection:
#     result = connection.execute('SELECT * FROM your_table LIMIT 10')
#     for row in result:
#         print(row)
#
#
# from sqlalchemy import create_engine
#
#
# conn_str = 'ibm_db_sa://_:_:_/BLUDB'


# # Create engine
# engine = create_engine(conn_str)
#
# # Connect to the database and execute a query
# with engine.connect() as connection:
#     result = connection.execute('SELECT * FROM your_table LIMIT 10')
#     for row in result:
#         print(row)
#


# import ibm_db_dbi
#
# # Define your connection string
# conn_str = 'DATABASE=bludb;HOSTNAME=_;PORT=50000;PROTOCOL=TCPIP;UID=_;PWD=_;'
#
# # Create a connection
# conn = ibm_db_dbi.connect(conn_str, '', '')
#
# # Example query
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM your_table LIMIT 10')
# for row in cursor.fetchall():
#     print(row)

# import ibm_db
# #use connection string
# conn=ibm_db.connect("DATABASE=database;HOSTNAME=hostname;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password",'','')
#
# #use connection string with JWT access token
# conn=ibm_db.connect("DATABASE=database;HOSTNAME=hostname;PORT=port;accesstoken=complete_access_token;authentication=token;accesstokentype=jwt;",'','')
#
# #use options
# options = { ibm_db.SQL_ATTR_INFO_PROGRAMNAME : 'TestProgram', ibm_db.SQL_ATTR_CURRENT_SCHEMA : 'MYSCHEMA' }
# conn=ibm_db.connect("DATABASE=database;HOSTNAME=hostname;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password",'','', options)
#



#
# dsn_hostname = ""
# dsn_uid = ""
# dsn_pwd = ""
#
# dsn_driver = "{IBM DB2 ODBC DRIVER}"
# dsn_database = "BLUDB"
# dsn_port = ""
# dsn_protocol = "TCPIP"
# dsn_security = "SSL"
#
# dsn = (
#     "DRIVER={0};"
#     "DATABASE={1};"
#     "HOSTNAME={2};"
#     "PORT={3};"
#     "PROTOCOL={4};"
#     "UID={5};"
#     "PWD={6};"
#     "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)
#
# #print the connection string to check correct values are specified
# print(dsn)
#
# try:
#     conn = ibm_db.connect(dsn, "", "")
#     print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
#
# except:
#     print ("Unable to connect: ", ibm_db.conn_errormsg() )
#
#
# server = ibm_db.server_info(conn)
#
# print ("DBMS_NAME: ", server.DBMS_NAME)
# print ("DBMS_VER:  ", server.DBMS_VER)
# print ("DB_NAME:   ", server.DB_NAME)
#
#
# client = ibm_db.client_info(conn)

# print ("DRIVER_NAME:          ", client.DRIVER_NAME)
# print ("DRIVER_VER:           ", client.DRIVER_VER)
# print ("DATA_SOURCE_NAME:     ", client.DATA_SOURCE_NAME)
# print ("DRIVER_ODBC_VER:      ", client.DRIVER_ODBC_VER)
# print ("ODBC_VER:             ", client.ODBC_VER)
# print ("ODBC_SQL_CONFORMANCE: ", client.ODBC_SQL_CONFORMANCE)
# print ("APPL_CODEPAGE:        ", client.APPL_CODEPAGE)
# print ("CONN_CODEPAGE:        ", client.CONN_CODEPAGE)


############################################################
# import ibm_db
# #Replace the placeholder values with the actuals for your Db2 Service Credentials
# dsn_hostname = ""
# dsn_uid = ""
# dsn_pwd = ""
# dsn_driver = "{IBM DB2 ODBC DRIVER}"
# dsn_database = "BLUDB"
# dsn_port = "50000"
# dsn_protocol = "TCPIP"
# dsn_security = "SSL"
# #Create database connection
# #DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
# dsn = (
#     "DRIVER={0};"
#     "DATABASE={1};"
#     "HOSTNAME={2};"
#     "PORT={3};"
#     "PROTOCOL={4};"
#     "UID={5};"
#     "PWD={6};"
#     "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)
#
# try:
#     conn = ibm_db.connect(dsn, "", "")
#     print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
#
# except:
#     print ("Unable to connect: ", ibm_db.conn_errormsg() )
#
#
# #Create database connection
# #DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
# dsn = (
#     "DRIVER={0};"
#     "DATABASE={1};"
#     "HOSTNAME={2};"
#     "PORT={3};"
#     "PROTOCOL={4};"
#     "UID={5};"
#     "PWD={6};"
#     "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)
#
# try:
#     conn = ibm_db.connect(dsn, "", "")
#     print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
#
# except:
#     print ("Unable to connect: ", ibm_db.conn_errormsg() )
#
#
# createQuery = "create table INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2))"
#
# createStmt = ibm_db.exec_immediate(conn,createQuery)
#
#
#
# insertQuery = "insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')"
#
# insertStmt = ibm_db.exec_immediate(conn, insertQuery)
# insertStmt = ibm_db.exec_immediate(conn, insertQuery)
#
# insertQuery2 = "insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')"
#
# insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)
#
#
#
# selectQuery = "select * from INSTRUCTOR"
#
# #Execute the statement
# selectStmt = ibm_db.exec_immediate(conn, selectQuery)
#
# #Fetch the Dictionary (for the first row only)
# ibm_db.fetch_both(selectStmt)
#
# #Fetch the rest of the rows and print the ID and FNAME for those rows
# while ibm_db.fetch_row(selectStmt) != False:
#    print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FNAME"))
#
# while ibm_db.fetch_row(selectStmt) != False:
#     print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FNAME"))
#
#

##################
# import pandas
# import ibm_db_dbi
#
# conn = ibm_db_dbi.Connection(conn)
# selectQuery = "select * from INSTRUCTOR"
#
# #retrieve the query results into a pandas dataframe
# pdf = pandas.read_sql(selectQuery, conn)
#
# #print just the LNAME for first row in the pandas data frame
# print(pdf.LNAME[0])
# print(pdf)
# print(pdf.shape)
#
# ibm_db.close(conn)



conn = sqlite3.connect('INSTRUCTOR.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS INSTRUCTOR")

table = "create table  IF NOT EXISTS INSTRUCTOR(ID INTEGER(2) PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARHCAR(20), CCODE CHAR(2))"
cur.execute(table)


cur.execute("insert into INSTRUCTOR values(1,'Rav','Ahul', 'Toronto', 'Ca')")
output = cur.fetchall()
print("want to print table?")

cur.execute("insert into INSTRUCTOR values(2, 'Raul', 'Chang', 'Markham', 'Ca'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US');")
statement = ('select * from INSTRUCTOR')
cur.execute(statement)

output = cur.fetchall()
for i in output:
    print(i)




