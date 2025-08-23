# Data base is a place where we can store data
# Rdatabase organized into tables 
# Tables Has columns
#There's Many Types of DataBAse (MongoGB,Mysql,Sqlie..)
#SQL Stand for Structured Query Language
#SQLite Can Run in Memory or A Singile File
#Data inside DataBase Has Types(Text,Integer,Date)


#############################################################################
# -------- Connect
#--------- Execute
#--------- Close


# import SQlite module
import sqlite3

# create Database and Connect----------------
db=sqlite3.connect("file01.db")

# Create The Tables and Fields
db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")


#Close Databe
db.close()