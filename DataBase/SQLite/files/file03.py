import sqlite3

db=sqlite3.connect("file03.db")
cr=db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS students (names TEXT, id INTEGER)")

students={
    "RACHID BOUBKER":1,
    "SAMIR HACHMI":2,
    "RIDWAN KARIM":3,
    "IMANE DOHA":4,
    "KARIMA SAMIR":5,
}
for key,value in students.items():
    cr.execute(f"INSERT INTO students(names,id) values('{key}',{value})")

#Fetch Data
# Fetchone => returns a single record or nome if no more rows are available
# Fetchall =>fetches all the rows of a query result it returns all the rows as a list of tuples. an empty list is returned if there is no record to frtch
# Fetchmany(size)=>...

cr.execute("SELECT names FROM students")
names=cr.fetchall()
print(cr.fetchone())
print("##############")
print(cr.fetchall())
print("############")
print(cr.fetchmany(3))

cr.execute("SELECT id FROM students")
print(cr.fetchone())
print("##############")
print(cr.fetchall())
print("############")
print(cr.fetchmany(3))

cr.execute("SELECT * FROM students")

print(cr.fetchone())
print("##############")
print(cr.fetchall())
print("############")
print(cr.fetchmany(3))


db.commit()

db.close()