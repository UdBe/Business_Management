# import mysql.connector as sqlcon

# mycon = sqlcon.connect(
# host = 'localhost',
# user = 'root',
# password = 'root',
# database = 'project'
# )

# mycur = mycon.cursor()

# mycur.execute("select sno from transact where name = 'Uday' ")
# mylist = (mycur.fetchone())[0]
# print(mylist)

import getpass

h = getpass.getpass(">>")
print(h)