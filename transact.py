import mysql.connector as sqlcon

mycon = sqlcon.connect(
host = 'localhost',
user = 'root',
password = 'root',
database = 'project'
)

mycur = mycon.cursor()

def addtrans(date,time,cname,totalval):
    mycur.execute("select sno from transact")
    mylist = mycur.fetchall()
    try: 
        sno = int(mylist[len(mylist)-1][0]) + 1
    except:
        sno = 1

    mycur.execute(("insert into transact values ({},'{}','{}','{}',{})").format(int(sno),str(date),str(time),str(cname),int(totalval)))
    mycon.commit()

def cont():
    ch = input("\nPress any key to continue: ")
    mainmenu()

def mainmenu():
    print("\n1. View Transactions")
    print("2. Sort Transactions")
    print("3. Main Menu")

    choice = int(input("Enter Choice: "))

    if choice == 1: 
        mycur.execute("select * from transact")
        mylist = mycur.fetchall()
        print("\nS.No.       Date        Time        Customer    Total Value(Rs/-)") 
        for k in mylist:
            for j in k:
                print(j, end = " " *(12 - len(str(j))) )
            print("")  
        cont()    

    elif choice == 2:
        print("\nSort Transactions by: ")
        print("1. Date")
        print("2. Customer Name")
        print("3. Total Value")
        ch1 = int(input("Enter Choice: "))
        
        if ch1 == 1:
            col = "date"
        elif ch1 == 2:
            col = "name"
        elif ch1 == 3:
            col = "value"
        else:
            print("Invalid Choice.")
            mainmenu()    

        print("\nSelect sort order: ")
        print("1. Ascending")
        print("2. Descending")

        ch2 = int(input("Enter Choice: "))
        
        if ch2 == 1:
            order = "ASC"
        elif ch2 == 2:
            order = "DESC"
        else:
            print("Invalid Choice.")
            mainmenu()    

        mycur.execute(("select * from transact order by {} {}").format(col,order))
        mylist = mycur.fetchall()
        print("\nS.No.       Date        Time        Customer    Total Value(Rs/-)") 
        for k in mylist:
            for j in k:
                print(j, end = " " *(12 - len(str(j))) )
            print("")  
        cont()  

    elif choice == 3:
        pass   

    else: 
        print("Invalid Choice")
        mainmenu()     


