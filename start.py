
from home import Profile 
from home import Home
obj=Profile()
h=Home()
'''
Title: Library Management system

Author: Abishek K

Created on: 01/02/2023

Last Modified Date: 20/02/2023

Reviewed on:  23/02/2023

Name of the reviewer:Silpa M

'''

print("\t\t________WELCOME________\n")
choice=int(input("1.Register\n2.Login\n"))
if choice==1:
    obj.register()
elif choice==2:
    obj.login()

