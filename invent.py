import mysql.connector as sqlcon

def cont():
    ch = input("\nPress any key to continue: ")
    askmenu()

def viewitem():

    print("\n1. View Entire Inventory ")
    print("2. View Specific Item")
    print("3. Apply conditions")
    
    ch = int(input("Enter choice: "))
 
    if ch == 1: 
        mycur.execute("select * from inventory")
        mylist = mycur.fetchall()
        print("\nS.No.       Name        Price       Quantity") 
        for k in mylist:
            for j in k:
                print(j, end = " " *(12 - len(str(j))) )
            print("")    
        cont()

    elif ch == 2:
        iname = str(input("Enter Item name: ")).strip()
        try:
            mycur.execute(("select * from inventory where name = '{}' ").format(iname))          
            mylist = mycur.fetchall()
            print("\nS.No.       Name        Price       Quantity") 
            for k in mylist:
                for j in k:
                    print(j, end = " " *(12 - len(str(j))) )
                print("")  
            cont()
        
        except:
            print("Item not found")
            cont()

    elif ch == 3: 
        cond = str(input("Input condition: ")).strip()

        try:
            mycur.execute(("select * from inventory where {} ").format(cond)) 
            mylist = mycur.fetchall()
            print("\nS.No.       Name        Price       Quantity") 
            for k in mylist:
                for j in k:
                    print(j, end = " " *(12 - len(str(j))) )
                print("")  
            cont()   
        except:
            print("Invalid Condition Entered")                   
            cont()
        
def additem():

    try: 
        iname = str(input("Item Name: ")).strip()
        iprice = int(input("Item Price: "))
        iqty = int(input("Item Quantity: "))

    except:             
        print("Invalid data entered ")
        additem()

    mycur.execute("select sno from inventory")
    mylist = mycur.fetchall()
    mylist2 = mylist[len(mylist)-1]
    mysno = mylist2[len(mylist2)-1] + 1

    mycur.execute(("insert into inventory values({} , '{}' , {}, {} )").format(mysno,iname,iprice,iqty))
    mycon.commit()

    ch = input("\nItem Added Successfully. Add more items? (y/n): ")
    if ch in "Yy":
        additem()
    elif ch in "Nn":
        askmenu()   
    else:
        print("Invalid Choice Entered. ")
        askmenu()

def updateitem():
    pass
    # name,category_to_be_updated, newvalue

def delitem():
    pass
    # name,quantity


mycon = sqlcon.connect(
    host = 'localhost',
    user = ' root ',
    password =  'root' ,
    database = 'project'
)
mycur = mycon.cursor()

def askmenu():
    print(" \n Welcome to Inventory \n")
    print("1. View Items")
    print("2. Add Items")
    print("3. Update Items")
    print("4. Delete Items")
    print("5. Main Menu ")
    ch = int(input("Enter Choice: "))

    if ch == 1: 
        viewitem()
        
    if ch == 2: 
        additem()
        
    if ch == 3: 
        updateitem()
        
    if ch == 4: 
        delitem()
        
    if ch == 5: 
        pass