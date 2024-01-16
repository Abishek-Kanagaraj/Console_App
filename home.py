from user_profile import Profile
import mysql.connector
from DB_connect import connection
mydb=connection()
mycursor = mydb.cursor()
class Home:
    
    def __init__(self) -> None:
        pass
    def home(self,usr_name):
        print("\t\t________HOME________\n")
        opt=int(input("1.Search bar\n2.Checkout(s)\n3.Sign out\n"))
        if opt==1:
            home.search(usr_name)
        elif opt==2:
            home.checkout(usr_name)
        elif opt==3:
            exit()
            

    def search(self,usr_name):
        global bk
        print("\t\t________SEARCH BAR________\n")
        bk=input("Search-'Book or Author name':\t")
        home.availability(bk,usr_name)
        
    def availability(self,bk_name,usr_name):
        l=[]
        flag=True
        val=True
        data=0
        mycursor.execute('select Book_name from issued')
        issued=mycursor.fetchall()
        for i in issued:
            if bk_name in i:
                val=False 
        if val==True:
            sql='select Book_name from books'
            mycursor.execute(sql)
            name=mycursor.fetchall()
            for i in name:
                if bk_name in i:
                    print('Available')
                    flag=False
                    
            mycursor.execute('select Author from books')
            author=mycursor.fetchall()
            for j in author:
                if bk_name in j:
                    query='select Book_name from books where Author=%s'
                    mycursor.execute(query,j)
                    for k in mycursor:
                        print(f'Available:{k}')
                        flag=False
                        data=1
                    break
        if flag == True:
            print("Not Available!!!")
            home.home(usr_name)
        elif data==1:
            home.search(usr_name)
        else:
            home.issue(bk_name,usr_name)
                    
            

    def issue(self,bk1,usr_name):
        l=[]
        bk=[]
        bk.append(bk1)
        choice=input("Do you want to afford it?\n1.Yes\n2.No\n")
        if choice=='1':
            sql='select Book_ID from books where Book_name=%s'
            mycursor.execute(sql,bk)
            issued=mycursor.fetchone()
            for i in issued:
                l.append(i)
            
            ql='select Book_name from books where Book_name=%s'
            mycursor.execute(ql,bk)
            issue=mycursor.fetchone()
            for i in issue:
                l.append(i)
            sq='select Author from books where Book_name=%s'
            mycursor.execute(sq,bk)
            iss=mycursor.fetchone()
            for i in iss:
                l.append(i)
            l.append(usr_name)
            query='insert into issued (Book_ID,Book_name,Author,Username,Issued_date,Due_date) values(%s,%s,%s,%s,CURDATE(),CURDATE()+15)'
            mycursor.execute(query,l)
            mydb.commit()
            print("Your book is issued.")
            home.home(usr_name)
        elif choice=='2':
            home.home(usr_name)
    def checkout(self,usr_name):
        l=[]
        l.append(usr_name)
        query='select * from issued where Username=%s'
        mycursor.execute(query,l)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        home.home(usr_name)        
                    
                    
obj1=Profile()   
home=Home()




           