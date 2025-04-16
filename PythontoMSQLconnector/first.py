import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", password = "Enivet@2")

if conn.is_connected():
    print("Connection Established")
print(conn)