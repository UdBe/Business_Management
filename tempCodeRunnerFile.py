mycur.execute("select sno from transact")
mylist = mycur.fetchall()
print(mylist[len(mylist)-1][0])
