import mysql.connector

def get_mysql_connection():
    try:
        cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="ccbpiedade")
        return cnx
    except mysql.connector.Error as err:
        print("Algo deu errado ao conectar ao MySQL: {}".format(err))
        return None
