import mysql.connector as sqlcon 
mycon = sqlcon.connect(
    host = 'localhost',
    user = ' root ',
    password =  'root' ,
    database = 'project'
)

mycur = mycon.cursor()
i = input("")
mycur.execute(("select quantity from inventory where name = '{}'").format(str(i).strip()))
mylist = mycur.fetchone()

print(mylist[0])