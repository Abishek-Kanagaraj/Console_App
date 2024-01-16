import mysql.connector
def connection():
    mydb=mysql.connector.connect(host='localhost',user='Abishek',passwd='1234',database='book_list')
    return mydb

        
    
    