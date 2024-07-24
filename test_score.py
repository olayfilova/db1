import csv, sqlite3

import inline
import matplotlib

conn = sqlite3.connect('SQLiteMagic.db')

cur = conn.cursor()
cur.execute('Drop table if exists INTERNATIONAL_STUDENT_TEST_SCORES')

table = 'create table if not exists INTERNATIONAL_STUDENT_TEST_SCORES(country VARCHAR(50), first_name VARCHAR(50), last_name VARCHAR(50), test_score INTEGER(2))'
cur.execute(table)
# print("INTERNATIONAL_STUDENT_TEST_SCORES TABLE")


cur.execute( "insert into INTERNATIONAL_STUDENT_TEST_SCORES values ( 'United States', 'Marshall', 'Bernadot', 54)")
statement = 'select * from INTERNATIONAL_STUDENT_TEST_SCORES'
cur.execute(statement)
output1 = cur.fetchall()
for i in output1:
    print(i)

cur.execute("insert into INTERNATIONAL_STUDENT_TEST_SCORES values ('Ghana', 'Celinda', 'Malkin', 51), ('Ukraine', 'Guillermo', 'Furze', 53), ('Greece', 'Aharon', 'Tunnow', 48), ('Poland', 'Cole', 'Winteringham', 49), ('Russia', 'Bail', 'Goodwin', 46), ('Sweden', 'Emlyn', 'Erricker', 55), ('Russia', 'Cathee', 'Sivewright', 49),('China', 'Barny', 'Ingerson', 57)")

statement = 'select * from INTERNATIONAL_STUDENT_TEST_SCORES'
cur.execute(statement)
output2 = cur.fetchall()
for i in output2:
    print(i)

cur.execute("insert into INTERNATIONAL_STUDENT_TEST_SCORES values ('Uganda', 'Sharla', 'Papaccio', 55),('China', 'Stella', 'Youens', 51),('Poland', 'Auroora', 'Stiffell', 45),('China', 'Clarita', 'Huet', 52),('Poland', 'Shannon', 'Goulden', 45),('Philippines', 'Emylee', 'Privost', 50),('France', 'Madelina', 'Burk', 49),('China', 'Saunderson', 'Root', 58),('Indonesia', 'Bo', 'Waring', 55),('China', 'Hollis', 'Domotor', 45),('Russia', 'Robbie', 'Collip', 46),('Philippines', 'Davon', 'Donisi', 46),('China', 'Cristabel', 'Radeliffe', 48),('China', 'Wallis', 'Bartleet', 58),('Moldova', 'Arleen', 'Stailey', 38),('Ireland', 'Mendel', 'Grumble', 58),('China', 'Sallyann', 'Exley', 51),('Mexico', 'Kain', 'Swaite', 46),('Indonesia', 'Alonso', 'Bulteel', 45),('Armenia', 'Anatol', 'Tankus', 51),('Indonesia', 'Coralyn', 'Dawkins', 48),('China', 'Deanne', 'Edwinson', 45),('China', 'Georgiana', 'Epple', 51),('Portugal', 'Bartlet', 'Breese', 56),('Azerbaijan', 'Idalina', 'Lukash', 50),('France', 'Livvie', 'Flory', 54),('Malaysia', 'Nonie', 'Borit', 48)")
statement = "select * from INTERNATIONAL_STUDENT_TEST_SCORES"
cur.execute(statement)
output3 = cur.fetchall()
for k in output3:
    print(k)


cur.execute("insert into INTERNATIONAL_STUDENT_TEST_SCORES values ('Indonesia', 'Clio', 'Mugg', 47),('Brazil', 'Westley', 'Measor', 48),('Philippines', 'Katrinka', 'Sibbert', 51),('Poland', 'Valentia', 'Mounch', 50),('Norway', 'Sheilah', 'Hedditch', 53),('Papua New Guinea', 'Itch', 'Jubb', 50),('Latvia', 'Stesha', 'Garnson', 53)")
statement = 'select* from INTERNATIONAL_STUDENT_TEST_SCORES'
cur.execute(statement)
output4 = cur.fetchall()
for i in output4:
    print (i)

cur.execute("insert into INTERNATIONAL_STUDENT_TEST_SCORES values('Canada', 'Cristionna', 'Wadmore', 46),('China', 'Lianna', 'Gatward', 43),('Guatemala', 'Tanney', 'Vials', 48)")
statement = "select * from INTERNATIONAL_STUDENT_TEST_SCORES"
cur.execute(statement)
out5= cur.fetchall()
for i in out5:
    print(i)

cur.execute("insert into INTERNATIONAL_STUDENT_TEST_SCORES values ('France', 'Alma', 'Zavittieri', 44),('China', 'Alvira', 'Tamas', 50),('United States', 'Shanon', 'Peres', 45),('Sweden', 'Maisey', 'Lynas', 53),('Indonesia', 'Kip', 'Hothersall', 46),('China', 'Cash', 'Landis', 48),('Panama', 'Kennith', 'Digance', 45), ('China', 'Ulberto', 'Riggeard', 48),('Switzerland', 'Judy', 'Gilligan', 49),('Philippines', 'Tod', 'Trevaskus', 52),('Brazil', 'Herold', 'Heggs', 44),('Latvia', 'Verney', 'Note', 50),('Poland', 'Temp', 'Ribey', 50),('China', 'Conroy', 'Egdal', 48),('Japan', 'Gabie', 'Alessandone', 47),('Ukraine', 'Devlen', 'Chaperlin', 54),('France', 'Babbette', 'Turner', 51),('Czech Republic', 'Virgil', 'Scotney', 52),('Tajikistan', 'Zorina', 'Bedow', 49),('China', 'Aidan', 'Rudeyeard', 50),('Ireland', 'Saunder', 'MacLice', 48),('France', 'Waly', 'Brunstan', 53)")
statement = "select * from INTERNATIONAL_STUDENT_TEST_SCORES"
cur.execute(statement)
outcome6 = cur.fetchall()
for k in outcome6:
    print(i)


cur.execute("insert into INTERNATIONAL_STUDENT_TEST_SCORES values ('China', 'Gisele', 'Enns', 52),('Peru', 'Mina', 'Winchester', 48),('Japan', 'Torie', 'MacShirrie', 50),('Russia', 'Benjamen', 'Kenford', 51),('China', 'Etan', 'Burn', 53),('Russia', 'Merralee', 'Chaperlin', 38),('Indonesia', 'Lanny', 'Malam', 49),('Canada', 'Wilhelm', 'Deeprose', 54),('Czech Republic', 'Lari', 'Hillhouse', 48),('China', 'Ossie', 'Woodley', 52),('Macedonia', 'April', 'Tyer', 50),('Vietnam', 'Madelon', 'Dansey', 53),('Ukraine', 'Korella', 'McNamee', 52),('Jamaica', 'Linnea', 'Cannam', 43),('China', 'Mart', 'Coling', 52),('Indonesia', 'Marna', 'Causbey', 47),('China', 'Berni', 'Daintier', 55),('Poland', 'Cynthia', 'Hassell', 49),('Canada', 'Carma', 'Schule', 49),('Indonesia', 'Malia', 'Blight', 48),('China', 'Paulo', 'Seivertsen', 47),('Niger', 'Kaylee', 'Hearley', 54),('Japan', 'Maure', 'Jandak', 46),('Argentina', 'Foss', 'Feavers', 45),('Venezuela', 'Ron', 'Leggitt', 60),('Russia', 'Flint', 'Gokes', 40),('China', 'Linet', 'Conelly', 52), ('Philippines', 'Nikolas', 'Birtwell', 57), ('Poland', 'Julio', 'Buesden', 48),('United States', 'Tiffie', 'Cosely', 58),('Australia', 'Eduard', 'Leipelt', 53)" )

statement = "select * from INTERNATIONAL_STUDENT_TEST_SCORES"
cur.execute(statement)
output8 = cur.fetchall()
for i in output8:
    print(i)


print("result")
country = "Canada"
statement = 'select * from INTERNATIONAL_STUDENT_TEST_SCORES where country = "Canada"'
cur.execute(statement)
output_res = cur.fetchall()
for i in output_res:
    print(i)


test_score_distribution = "select test_score as Test_Score, count(*) as Frequency from INTERNATIONAL_STUDENT_TEST_SCORES group by test_score;"
cur.execute(test_score_distribution)
output_py = cur.fetchall()
for i in output_py:
    print(i)

import pandas as pd

# dataframe = test_score_distribution.DataFrame()
# %matplotlib inline
# import seaborn
#
# plot = seaborn.barplot(x='Test_Score',y='Frequency', data=dataframe)










