import mysql.connector as sqlcon

mycon = sqlcon.connect(
host = 'localhost',
user = 'root',
password = 'root',
database = 'project'
)

mycur = mycon.cursor()

mycur.execute("select sno from transact")
mylist = mycur.fetchall()
try:
    print(mylist[len(mylist)-1][0])
except: 
    print("1")
