import mysql.connector as sqlcon 
mycon = sqlcon.connect(
    host = 'localhost',
    user = ' root ',
    password =  'root' ,
    database = 'project'
)

mycur = mycon.cursor()

mycur.execute("select name from inventory")         
mylist = mycur.fetchone()
print(mylist)

