import mysql.connector as sqlcon 
mycon = sqlcon.connect(
    host = 'localhost',
    user = ' root ',
    password =  'root' ,
    database = 'project'
)

mycur = mycon.cursor()

mycur.execute("select sno from inventory")         
mylist = mycur.fetchall()
mylist2 = mylist[len(mylist)-1]
mysno = mylist2[len(mylist2)-1] + 1
print(mysno)
