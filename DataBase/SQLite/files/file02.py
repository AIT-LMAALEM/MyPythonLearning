import sqlite3

# create Database and Connect----------------
db=sqlite3.connect("file01.db")

# Setting Up The Cursor
Cr=db.cursor()
Cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
Cr.execute("CREATE TABLE IF NOT EXISTS useres (user_id INTEGER, name TEXT)")


# Inserting Data

#method 1
# Cr.execute("INSERT INTO useres(user_id, name) values(1,'Ahmed')")
# Cr.execute("INSERT INTO useres(user_id, name) values(2,'Samir')")
# Cr.execute("INSERT INTO useres(user_id, name) values(3,'Rachid')")

#method 2
my_list=["Anour","Imane","Yassine","Omar","Amina","Ridwane","Radi"]

for key,user in enumerate(my_list):
    Cr.execute(f"INSERT INTO useres(user_id,name) values({key+1},'{user}')")

#Save (Commit ) Changes
db.commit()

#Close Databe
db.close()