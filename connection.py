import mysql.connector

try:
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="ccbpiedade")
except mysql.connector.Error as err:
    print("Algo deu errado: {}".format(err))