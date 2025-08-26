import sqlite3

def get_all_data():
    try:
        #Connect to Database
        db=sqlite3.connect("file03.db")
        print("Connecter to DataBase  Successfully")
        #setting up the Cursor
        cr=db.cursor()
        # Fetch Data from Database
        cr.execute("SELECT * FROM students")
        # Assing Data from Variable
        result=cr.fetchmany(5)
        for name,id in result:
            print(f"Student {name} has id:{id}")
        # Print Number of Rows
        print(f"Data base has {len(result)} rows")


    except sqlite3.Error as er:
        print(f"Error Reading Data:{er}")
    finally:
        if (db):
            #close Database connection
            db.close()
            print("Connection to Database is close")


get_all_data()