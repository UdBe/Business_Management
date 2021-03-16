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

def manageuser():

    print("\nSelect Option: ")
    print("1. Create New User")
    print("2. View Users")
    print("3. Delete User")
    
    option = int(input("Enter Option: "))

    if option == 1: 
        userid = input("\nEnter Username: ")
        pass1 = input("Enter Password: ")
        pass2 = input("Confirm Password: ")

        if pass1 == pass2: 
            pass
        else: 
            print("Passwords do not match. Try Again. ")
            manageuser()

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
            manageuser()
    
    elif option == 2: 
        mycur.execute("select username,role from login")
        mylist = mycur.fetchall() 
        print("List of Users: ")
        for i in mylist: 
            if i[1] == 1:
                str1 = "Admin"
            elif i[1] == 2: 
                str1 = "Manager" 
            else:
                str1 = "Employee/Cashier"    

            print(i[0]," " * (12 - len(i[0])) ," : ",str1)
        input("Press Enter to continue: ")
        mainmenu1()    

    elif option == 3:
        mycur.execute("select username,role from login")
        mylist = mycur.fetchall() 
        mylist2 = [] 
        print("List of Users: ")
        for i in mylist: 
            if i[1] == 1:
                continue
            else:    
                mylist2.append(i[0])
                print(i[0])
        
        print("\nNote: Admin accounts cannot be deleted \n") 
        name = str(input("Enter Username to be deleted: "))

        if name in mylist2: 
            mycur.execute(("Delete from login where username = '{}' ").format(name))
            mycon.commit()
        
            print("User Deleted successfully. ")
            input("Press Enter to continue")
            mainmenu1() 
        else:
            print("Invalid user. Try again. ")
            manageuser()       

    else: 
        print("Invalid choice. Try Again ")
        manageuser()


def viewacc():
    mycur.execute("select username,role from login")
    mylist = mycur.fetchall() 
    print("List of Users: ")
    for i in mylist: 
        if i[1] == 1:
            str1 = "Admin"
        elif i[1] == 2: 
            str1 = "Manager" 
        else:
            str1 = "Employee/Cashier"    

        print(i[0]," " * (12 - len(i[0])) ," : ",str1)
    input("Press Enter to continue: ")
    mainmenu2()    



def mainmenu1():
   
    print("\nWelcome!! \n ")
    print("1. Generate Billing Details ")
    print("2. Manage Inventory ")
    print("3. View Transaction History ")
    print("4. Manage User Accounts")
    print("5. Exit \n ")
    
    choice = int(input( "Enter Choice: "))
    if choice == 1: 
        billing.genbill()
        mainmenu1()
    elif choice == 2: 
        invent.askmenu()
        mainmenu1()  
    elif choice == 3: 
        transact.mainmenu()
        mainmenu1()
    elif choice == 4: 
        manageuser()
    elif choice == 5: 
        sys.exit()
    else: 
        print("Invalid Choice")
        mainmenu1()

def mainmenu2():
   
    print("\nWelcome!! \n ")
    print("1. Generate Billing Details ")
    print("2. Manage Inventory ")
    print("3. View Transaction History ")
    print("4. View User Accounts")
    print("5. Exit \n ")
    
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
        viewacc()
    elif choice == 5: 
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
    print("\nLogin")
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


