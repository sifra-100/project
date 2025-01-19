import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)
cursor.execute('''Insert into STUDENT values('Divy','Data Science','A',90)''')
cursor.execute('''Insert into STUDENT values('Krutarth','Data Science','B',100)''')
cursor.execute('''Insert into STUDENT values('Sahil','Data Science','A',86)''')
cursor.execute('''Insert into STUDENT values('Vishv','DEVOPS','A',50)''')
cursor.execute('''Insert into STUDENT values('Krish','DEVOPS','A',35)''')

print("The inserted records are")
data=cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)
connection.commit()
connection.close()