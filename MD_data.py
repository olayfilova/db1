# import pandas as pd
# import sqlite3
# import matplotlib.pyplot as plt
# import seaborn as sns
# mysql> SOURCE C:/temp/sakila-db/sakila-schema.sql;
# mysql> SOURCE C:/temp/sakila-db/sakila-data.sql;


# data = pd.read_csv('./menu.csv')
# conn = sqlite3.connect ('McDonalds.db')
# data.to_sql('MCDONALDS_NUTRITION', conn)
#
# df= pd.read_sql("select * from MCDONALDS_NUTRITION", conn)
# print(df)

# sqlite3 sakila.db
# .read/path/to/sakila-schema.sql
# .read/path/to/sakila-data.sql
# .exit


# conn =sqlite3.connect('../db1/sakila-db/sakila-schema.sql')
# data = pd.read_sql('../db1/sakila-db/sakila-data.sql', conn)
# # conn =sqlite3.connect('/Users/olgafilova/Downloads/sakila-db')
# data.to_sql('/pythonProject2/db1/sakila-db', conn)

# plot = sns.joinplot(x = 'Protein', y = 'total Fat', data = df)
# plot.show()
#
# df1.head()
# df.describe( include = 'all')
# %matplotlib inline
#
# plot= sns.swarmplot(x = 'Category', y = 'Sodium', data =df)
# plot.setp(plot.get_xticklabels, rotation = 70)
# plt.title('Sodium Content')
# plt.show()
#
#
# df['Sodium'].describe()
# df['Sodium'].idxmax()
# df.at[82, 'Item']
#
#
# plot2= sns.setstyle("whitegrid")
# ax=sns.boxplot (x = df ["Sugar"])
# plot2.show()



