import sqlite3

db=sqlite3.connect("file03.db")
cr=db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS students (names TEXT, id INTEGER)")

#Fetch Data before Update
cr.execute("SELECT * FROM students")
results=cr.fetchmany(5)
for name,id in results:
    print(f"student {name} has id:{id}")


#Update Data
cr.execute("UPDATE students SET names ='MAHMOUD AIT TAOURIRT' WHERE id=1")
cr.execute("UPDATE students SET names ='RITAGE KARIM' WHERE id=3")
cr.execute("UPDATE students SET names ='ZAKARIA HACHMI' WHERE id=5")


#Fetch Data after Update
print("####################")
cr.execute("SELECT * FROM students")
results=cr.fetchmany(5)
for name,id in results:
    print(f"student {name} has id:{id}")


#Delete from Data
db.execute("DELETE FROM students WHERE id=5")        # DELETE FROM <table> WHERE <condition>.



db.commit()

db.close()