import ibm_db_sa
import sqlalchemy

from sqlalchemy import create_engine
#
# 
# conn_str = 'ibm_db_sa://_:_@_:_/BLUDB'
# engine = create_engine(conn_str)
# with engine.connect() as connection:
#     result = connection.execute('SELECT * FROM your_table LIMIT 10')
#     for row in result:
#         print(row)

# ###imb_db
# # import ibm_db
# #
# #
# # dsn_hostname = "_"
# # dsn_uid = "_"
# # dsn_pwd = "_"
# #
# # dsn_driver = "{IBM DB2 ODBC DRIVER}"
# # dsn_database = "BLUDB"
# # dsn_port = "_"
# # dsn_protocol = "TCPIP"
# # dsn_security = "SSL"
# #
# # dsn = (
# #     "DRIVER={0};"
# #     "DATABASE={1};"
# #     "HOSTNAME={2};"
# #     "PORT={3};"
# #     "PROTOCOL={4};"
# #     "UID={5};"
# #     "PWD={6};"
# #     "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)
# #
# # #print the connection string to check correct values are specified
# # print(dsn)
# #
# # try:
# #     conn = ibm_db.connect(dsn, "", "")
# #     print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
# #
# # except:
# #     print ("Unable to connect: ", ibm_db.conn_errormsg() )
# #
#

# import sqlite3
# import pandas as pd

###SYSCAT.TABLES IN DB2
###sqlite_master,SHOW TABLES
###ATRIBUTE SQLITE:
###PRAGMA table_info([table_name])
###ATRIBUTE MYSQL
###DESCRIBE_TABLE

# import matplotlib.pyplot as plt
# #/ % matplotlib inline
# # import seaborn as sns
#
# import pandas as pd
# import sqlite3
#
#
# url = 'https://data.cityofchicago.org/resource/jcxq-k9xf.csv'
# df = pd.read_csv(url)
# con = sqlite3.connect('chicago_data.db')
# df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False, method='multi')
#
#
# # print table_name
# def print_table_name(con):
#     cur = con.cursor()
#     cur.execute("SELECT name FROM sqlite_master WHERE type ='table';")
#     tables = cur.fetchall()
#     print("Table in database")
#     for table in tables:
#         table_name = table[0]
#         print(f' - {table_name}')
#     cur.close()
#
# # all rows count
# def count_row_all_table(con):
#     cur= con.cursor()
#     cur.execute("SELECT name FROM sqlite_master WHERE type ='table';")
#     tables = cur.fetchall()
#
#     table_counts = {}
#     for table in tables:
#         table_name = table[0]
#         try:
#             print(f'Counting rows in - {table_name}')
#             cur.execute(f'SELECT COUNT (*) FROM "{table_name}";')
#             row_count = cur.fetchone()[0]
#             table_counts[table_name] = row_count
#         except sqlite3.OperationalError as e:
#             print(f'ERROR in counting {table_name}: {e}')
#
#     cur.close()
#     return table_counts
#
# print_table_name(con)
#
# table_counts = count_row_all_table(con)
# for table, counts in table_counts.items():
#     print(f'table:{table}, number of rows:{counts}')
#
# con.close()
#
#
#
# con = sqlite3.connect("socioeconomic.db")
# cur = con.cursor()
# # /!pip install -q pandas==1.1.5
# # /%sql sqlite3:///socioeconomic.db
#
# import pandas as pd
# df1 = pd.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
# df1.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index= False, method='multi')
#
#
# statement ="SELECT * FROM chicago_socioeconomic_data LIMIT 5;"
# cur = con.cursor()
# cur.execute(statement)
# out = cur.fetchmany(5)
# for i in out:
#     print(i)
#
# # heading
# print(df.head())
# con.close()
#
# url = 'https://data.cityofchicago.org/resource/jcxq-k9xf.csv'
# df = pd.read_csv(url)
#
# con = sqlite3.connect("socioeconomic.db")
# cur = con.cursor()
# df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False, method='multi')
#
# statement = "SELECT COUNT(DISTINCT ca) FROM chicago_socioeconomic_data WHERE hardship_index>50.0"
# cur.execute(statement)
# output = cur.fetchall()
# for i in output:
#     print(i)
# cur.close()
#
#
# df = pd.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
#
# con = sqlite3.connect("socioeconomic.db")
# cur = con.cursor()
# df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False, method='multi')
# statement1 = "SELECT MAX(hardship_index) FROM chicago_socioeconomic_data"
# statement2 = "SELECT * FROM chicago_socioeconomic_data WHERE hardship_index = (SELECT MAX (hardship_index) FROM chicago_socioeconomic_data)"
# cur.execute(statement1)
# output = cur.fetchall()
# for i in output:
#     print(i)
#
# statement3 = "SELECT community_area_name  FROM chicago_socioeconomic_data WHERE  hardship_index =  (SELECT MAX(hardship_index) FROM chicago_socioeconomic_data)"
# cur.execute(statement3)
# output = cur.fetchone()
# print(output)
#
#
# statement4 = "SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_>60000"
# cur.execute(statement4)
# res = cur.fetchall()
# print(f'Areas with per_capita_income grater than 60,00 are: {res}')
#
#
#
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df = pd.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
# con = sqlite3.connect("socioeconomic.db")
# cur=con.cursor()
# df.to_sql("chicago_socioeconomic_data", con,if_exists='replace', index=False, method='multi' )
#
# income_vs_hardship = "SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;"
# cur.execute(income_vs_hardship)
# outcome = cur.fetchall()
#
#
# # jupiter
# # plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())
# # plt.show()
#
# columns = [desc[0] for desc in cur.description]
# df = pd.DataFrame(outcome, columns=columns)
#
# # Plot using seaborn
# plot = sns.jointplot(x='per_capita_income_', y='hardship_index', data=df)
# plt.show()
#
# # Close the cursor and connection
# cur.close()
# con.close()


####
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # Create a sample DataFrame
# data = {
#     'Test_Score': ['A', 'B', 'C', 'D', 'F'],
#     'Frequency': [50, 40, 30, 20, 10]
# }
# dataframe = pd.DataFrame(data)
#
# # Create a bar plot
# sns.barplot(x='Test_Score', y='Frequency', data=dataframe)
#
# # Display the plot
# plt.show()
#
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # Create a sample DataFrame
# data = {
#     'Month': ['January', 'February', 'March', 'April', 'May', 'June',
#               'July', 'August', 'September', 'October', 'November', 'December'],
#     'Average_Temperature': [30.5, 32.0, 45.5, 55.0, 65.5, 75.0, 80.5, 78.0, 70.0, 60.0, 50.0, 35.0]
# }
# dataframe = pd.DataFrame(data)
#
# # Create a bar plot
# sns.barplot(x='Month', y='Average_Temperature', data=dataframe)
#
# # Rotate the x labels for better readability
# plt.xticks(rotation=45)
#
# # Add a title and labels
# plt.title('Average Monthly Temperatures')
# plt.xlabel('Month')
# plt.ylabel('Average Temperature (°F)')
#
# # Display the plot
# plt.show()


import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

# Create a sample DataFrame
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14],
    'z': [5, 6, 7, 8, 9],
    'color': ['A', 'B', 'C', 'D', 'E'],
    'size': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Create an interactive 3D scatter plot
fig = px.scatter_3d(df, x='x', y='y', z='z',
                    color='color', size='size',
                    title='Interactive 3D Scatter Plot')

# Show the plot
fig.show()

# import plotly.express as px
# import pandas as pd
#
# # Create a sample DataFrame
# data = {
#     'x': [1, 2, 3, 4, 5],
#     'y': [10, 11, 12, 13, 14],
#     'z': [5, 6, 7, 8, 9],
#     'color': ['A', 'B', 'C', 'D', 'E'],
#     'size': [100, 200, 300, 400, 500]
# }
# df = pd.DataFrame(data)
#
# # Create an interactive 3D scatter plot
# fig = px.scatter_3d(df, x='x', y='y', z='z',
#                     color='color', size='size',
#                     title='Interactive 3D Scatter Plot')
#
# # Show the plot
# fig.show()

# Community Area Number (ca): Used to uniquely identify each row of the dataset
# Community Area Name (community_area_name): The name of the region in the city of Chicago
# Percent of Housing Crowded (percent_of_housing_crowded): Percent of occupied housing units with more than one person per room
# Percent Households Below Poverty (percent_households_below_poverty): Percent of households living below the federal poverty line
# Percent Aged 16+ Unemployed (percent_aged_16_unemployed): Percent of persons over the age of 16 years that are unemployed
# Percent Aged 25+ without High School Diploma (percent_aged_25_without_high_school_diploma): Percent of persons over the age of 25 years without a high school education
# Percent Aged Under 18 or Over 64:Percent of population under 18 or over 64 years of age (percent_aged_under_18_or_over_64): (ie. dependents)
# Per Capita Income (per_capita_income_): Community Area per capita income is estimated as the sum of tract-level aggragate incomes divided by the total population
# Hardship Index (hardship_index): Score that incorporates each of the six selecte



