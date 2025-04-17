import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", password = "Enivet@2")

if conn.is_connected():
    print("Connection Established")
print()

mycursor = conn.cursor()
# mycursor.execute('show databases')
# myresult = mycursor.fetchall()
# for x in mycursor:
#     print(mycursor)
    
    
mycursor.execute('use pythondb')
mycursor.execute("create table student(name varchar(50), branch varchar(10), id int")
mycursor.execute("show tables")

for x in mycursor:
    print(x)