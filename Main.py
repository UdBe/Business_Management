import mysql.connector as sqlcon
import invent
import billing
import transact
import sys
import getpass

mycon = sqlcon.connect(
host = 'localhost',
user = ' root ',
password =  'root' ,
database = 'project'
)
mycur = mycon.cursor()

def createuser():
    userid = input("\nEnter Username: ")
    pass1 = input("Enter Password: ")
    pass2 = input("Confirm Password: ")

    if pass1 == pass2: 
        pass
    else: 
        print("Passwords do not match. Try Again. ")
        createuser()

    print("\nChoose Role: ")    
    print("1. Administrator/Owner ")  
    print("2. Manager ")  
    print("3. Cashier/Employee ")  
    
    roleint = int(input("Enter Choice: "))
    if roleint == 1 or roleint == 2 or roleint == 3: 
        mycur.execute(("insert into login values ('{}' , '{}', {} ) ").format(str(userid),str(pass1),int(roleint)))
        mycon.commit()
        print(("User {} created successfullly. ").format(userid))
        input("\nPress Enter to continue: ")
        mainmenu1()
    else:
        print('Invalid Choice. Try Again.')
        createuser()

def mainmenu1():
   
    print("\nWelcome!! \n ")
    print("1. Generate Billing Details ")
    print("2. Manage Inventory ")
    print("3. Security Vault  ")
    print("4. View Transaction History ")
    print("5. Create User Accounts")
    print("6. Exit \n ")
    
    choice = int(input( "Enter Choice: "))
    if choice == 1: 
        billing.genbill()
        mainmenu1()
    elif choice == 2: 
        invent.askmenu()
        mainmenu1()  
    elif choice == 3: 
        pass
    elif choice == 4: 
        transact.mainmenu()
        mainmenu1()
    elif choice == 5: 
        createuser()
    elif choice == 6: 
        sys.exit()
    else: 
        print("Invalid Choice")
        mainmenu1()

def mainmenu2():
   
    print("\nWelcome!! \n ")
    print("1. Generate Billing Details ")
    print("2. Manage Inventory ")
    print("3. View Transaction History ")
    print("4. Exit \n ")
    
    choice = int(input( "Enter Choice: "))
    if choice == 1: 
        billing.genbill()
        mainmenu3()
    elif choice == 2: 
        invent.askmenu()
        mainmenu3()  
    elif choice == 3: 
        transact.mainmenu()
        mainmenu3()
    elif choice == 4: 
        sys.exit()
    else: 
        print("Invalid Choice")
        mainmenu3()

def mainmenu3():
   
    print("\nWelcome!! \n ")
    print("1. Generate Billing Details ")
    print("2. Exit \n ")
    
    choice = int(input( "Enter Choice: "))
    if choice == 1: 
        billing.genbill()
        mainmenu3()
    elif choice == 2: 
        sys.exit()
    else: 
        print("Invalid Choice")
        mainmenu3()


def login():
    print("Login")
    user = input( "\nEnter Username: ")

    userlist = [] 

    mycur.execute("select username from login")
    mylist = mycur.fetchall()
    for i in mylist: 
        userlist.append(i[0])

    if user in userlist:
        pass
    else:
        print("User not found. Try Again.")
        login()

    passwd = input( "Enter Password: ")

    mycur.execute(("select password from login where username = '{}' ").format(user))
    correctpass = (mycur.fetchone())[0]

    if str(correctpass) == str(passwd):
        pass
    else:
        print("Incorrect Password. Try Again. ")
        login()

    mycur.execute(("select role from login where username = '{}' ").format(user))
    role = (mycur.fetchone())[0]
    
    if role == 1:
        mainmenu1()
    elif role == 2:
        mainmenu2()
    elif role == 3:
        mainmenu3()

login()        


