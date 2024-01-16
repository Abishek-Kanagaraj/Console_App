import mysql.connector
from DB_connect import connection
mydb=connection()
mycursor = mydb.cursor()

class Profile:


    def __init__(self) -> None:
        pass
    def register(self):
        from validation import Validate
        obj3=Validate()
        print("\t\t________REGISTER________\n")
        username=(input("Username:\t"))
        password=(input("Password:\t"))
        obj3.validate(password)
        
        
        val=(username,password)
        query='insert into credentials values(%s,%s)'
        try:
            mycursor.execute(query,val)
            mydb.commit()
        except:
            print("User aldready exist")
            choice=int(input("1.Register\n2.Login\n"))
            if choice==1:
                obj1.register()
            elif choice==2:
                obj1.login()
        obj1.login()
    def login(self):
        from home import Home
        obj2=Home() 
        print("\t\t________LOGIN________\n")
        global usr_name
        usr_name=input("Username:\t")
        pass_word=input("Password:\t")
        mycursor.execute("select * from credentials")
        for i in mycursor:
            if i == (usr_name,pass_word):
                print("successfully logged in")
                obj2.search(usr_name)
        else:
            print("Incorrect username or password!!\n Enter valid Username and Password.")
            obj1.login()
            

obj1=Profile()