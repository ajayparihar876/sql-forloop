import sqlite3

dbname = input(" Enter the database NAME  ")
tablename = input("Enter the table name  ")
store = input("how many student you want to store  ")
# All value stored in var is string😁
# we want int datatype in store var
stored = int(store)
database = dbname+'.sqlite3'
# know we open a file🤑
fo = open(database, "a")

con = sqlite3.connect(database)
cur = con.cursor()
# table creating 😎
cur.execute(
    f"create table {tablename}(name text, email text, mobile text, address text)")
for x in range(stored):
    n = input("Enter the student name  ")
    m = input("Enter the email id   ")
    o = input("Enter the student mobile number  ")
    p = input("Enter the student Address  ")

    cur.execute(f"Insert into {tablename} VALUES ('{n}','{m}','{o}','{p}')")
con.commit()
con.close()
fo.close()
