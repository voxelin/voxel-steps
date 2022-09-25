import mysql.connector

mydb = mysql.connector.connect(
    host="containers-us-west-43.railway.app",
    user="root",
    passwd="yufRnskW2jIOpZY2kV1R",
    database="railway",
    port=8070
)

mycursor = mydb.cursor()

# (1, 'Jamine', 'Poulson', 'poulsonsoftware')
mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
    print(x[1], x[2])

mydb.close()