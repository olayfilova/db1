import csv, sqlite3
import pandas as pd


con= sqlite3.connect("RealWorldData.db")
cur=con.cursor()

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", con,if_exists='replace', index=False, method='multi')

## name of tables
# cur.execute('SELECT name FROM sqlite_master WHERE type = "table";')
# output = cur.fetchall()
# print(output)

##count ov rows
# statement = "SELECT COUNT (name) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');"
# cur.execute(statement)
# output2 = cur.fetchall()
# for i in output2:
#     print(i)
# print(output2)

# statement2 = "select name, type, length (type) from PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');"
# cur.execute(statement2)
# output = cur.fetchall()
# print(output)


# cur.execute('SELECT COUNT (*) FROM CHICAGO_PUBLIC_SCHOOLS_DATA where "Elementary, Middle, or High School"="ES";')
# output = cur.fetchall()
# print(output)

# cur.execute('select MAX(SAFETY_SCORE) as Maximum_SafetyScore from CHICAGO_PUBLIC_SCHOOLS_DATA')
# output = cur.fetchall()
# print(output)

# cur.execute('select Name_of_School, Safety_Score from CHICAGO_PUBLIC_SCHOOLS_DATA where Safety_Score = 99 ')
# output = cur.fetchall()
# print(output)

# cur.execute('select Name_of_School, Safety_Score from CHICAGO_PUBLIC_SCHOOLS_DATA where Safety_Score = (select MAX( Safety_Score) from CHICAGO_PUBLIC_SCHOOLS_DATA)')
#
# output = cur.fetchall()
# print(output)

cur.execute('select Name_of_School, Average_Student_Attendance from CHICAGO_PUBLIC_SCHOOLS_DATA \
    order by Average_Student_Attendance desc nulls last limit 10')
output = cur.fetchall()
print(output)

cur.execute('SELECT Name_of_School, Average_Student_Attendance  \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     order by Average_Student_Attendance \
     LIMIT 5')
output = cur.fetchall()
print(output)

cur.execute("SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     order by Average_Student_Attendance \
     LIMIT 5")
output = cur.fetchall()
print(output)

cur.execute("SELECT Name_of_School, Average_Student_Attendance  \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     where CAST ( REPLACE(Average_Student_Attendance, '%', '') AS DOUBLE ) < 70 \
     order by Average_Student_Attendance")
output = cur.fetchall()
print(output)

cur.execute('select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from CHICAGO_PUBLIC_SCHOOLS_DATA \
   group by Community_Area_Name')
output = cur.fetchall()
print(output)

cur.execute('select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from CHICAGO_PUBLIC_SCHOOLS_DATA \
   group by Community_Area_Name \
   order by TOTAL_ENROLLMENT asc \
   LIMIT 5 ')
output = cur.fetchall()
print(output)

cur.execute("SELECT name_of_school, safety_score \
FROM CHICAGO_PUBLIC_SCHOOLS_DATA  where safety_score !='None' \
ORDER BY safety_score \
LIMIT 5")
output = cur.fetchall()
print(output)

import pandas as pd
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv")
df.to_sql("CENSUS_DATA", con, if_exists='replace', index=False, method="multi")
con =sqlite3.connect("socioeconomic.db")


cur.execute("select hardship_index from CENSUS_DATA CD, CHICAGO_PUBLIC_SCHOOLS_DATA CPS\
    where CD.community_area_number = CPS.community_area_number\
    and college_enrollment = 4368")
output = cur.fetchall()
print(output)


cur.execute("select community_area_number, community_area_name, hardship_index from CENSUS_DATA \
   where community_area_number in \
   ( select community_area_number from CHICAGO_PUBLIC_SCHOOLS_DATA order by college_enrollment desc limit 1 )")
output = cur.fetchall()
print(output)
con.close()


con= sqlite3.connect("RealWorldData.db")
cur=con.cursor()
df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", con,if_exists='replace', index=False, method='multi')

cur.execute("select * from PRAGMA_TABLE_INFO ('CHICAGO_PUBLIC_SCHOOLS_DATA')")
output = cur.fetchall()
print(output)



