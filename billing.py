import mysql.connector as sqlcon
import datetime

mycon = sqlcon.connect(
host = 'localhost',
user = ' root ',
password =  'root' ,
database = 'project'
)

mycur = mycon.cursor()

ilist = [] 
snolist = [1]
qtylist = []
pricelist = [] 

def findprice(iname):
    mycur.execute(("select price from inventory where name = '{}'").format(iname))
    mylist = mycur.fetchone()
    return int(mylist[0])

def checkitemname(var):
    mycur.execute("select name from inventory")
    mylist = mycur.fetchall()
    mylist2 = []
    for k in mylist:
        for j in k:
            mylist2.append(j)
    if var in mylist2:
        return True
    else:
        return False


def checkitemqty(var1,var2):
    mycur.execute(("select quantity from inventory where name = '{}'").format(str(var1).strip()))
    mylist = mycur.fetchone()
    if var2 <= mylist[0]:
        qtylist.append(var2)
        return True
    else:
        return False


def viewall():
    mycur.execute("select * from inventory")
    mylist = mycur.fetchall()
    print("\nS.No.       Name        Price       Quantity") 
    for k in mylist:
        for j in k:
            print(j, end = " " *(12 - len(str(j))) )
        print("")  


def printitems():
    print("S.No.       Name        Quantity    Rate        Price") 
    for i in ilist:
        for k in i:
            print(k, end = " " *(12 - len(str(k))) )
        print("")  

def updateinventory(name,qty):
    
    myqty = int(qtylist[0])
    mycur.execute(("update inventory set quantity = {} where name = '{}' ").format(myqty,name))
    mycon.commit()
    qtylist.pop()

def printbill(name,date,time):

    totalprice = 0
    for i in pricelist:
        totalprice =     totalprice + int(i)

    print("\n-----------------------------------------------------")
    print("                 XYZ business/shop                ")
    print("-----------------------------------------------------")
    print("Name:   " + name)
    print("Date: " , date , "                     " ,"Time: " , time ,"")
    print("-----------------------------------------------------")
    printitems()
    print("-----------------------------------------------------")
    print("Total Price:                 " ,totalprice , "Rs/-" )
    print("-----------------------------------------------------")
    print("Thank you for shopping with us!")
    print("Customer care number: 9896xxxxxx")
    print("Email: XYZ@abc.com")
    print("Corporate office: A-12, PQR colony, New Delhi")
    print("-----------------------------------------------------")



def genbill():

    def addnewitems():
        
        viewall() 
        citem = str(input("Enter Item Name: ")).strip()
        if checkitemname(citem):
            pass
        else:
            print("Item does not exist.")
            genbill()
        
        cqty = int(input("Enter Quantity: "))
        
        if checkitemqty(citem,cqty):
            crate = findprice(citem)
            cprice = crate * cqty
        
        else:
            print("Not enough stock for item in inventory.")
            genbill()  

        i_list = [snolist[len(snolist) - 1],citem,cqty,crate,cprice]
        pricelist.append(cprice)
        ilist.append(i_list) 
        updateinventory(citem,cqty)
        #update transaction history  
        
        def askuser():
        
            ask = input('Add more items? (y/n)')
            if ask in 'Yy':
                newsno = snolist[len(snolist) - 1] + 1
                snolist.append(newsno)
                addnewitems()
            elif ask in 'Nn':
                printbill(cname,cdate,ctime)
            else: 
                print("Invalid option ")    
                askuser()      
        askuser()

    print("\nBilling Details")
    
    cdate = datetime.date.today()
    now = datetime.datetime.now()
    ctime = now.strftime("%H:%M")

    cname = str(input("\nEnter Customer Name: "))
    addnewitems()
       
