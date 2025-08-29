import sqlite3

db=sqlite3.connect("AppSkill.db")
Cr=db.cursor()
Cr.execute("CREATE TABLE IF NOT EXISTS skills(name TEXT, progress INTEGER, user_id INTEGER)")


# Commit and Close Function
def commit_and_close():
    db.commit()
    db.close()
    print("Connection To Database Is Close!")


input_messege="""
What Do you Want To Do?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update The App
"q" => Quit The App
Choose Option:
"""
# Input Option Choose
user_input=input(input_messege).strip().lower()
#Commands list
commands_list=["s","a","d","u","q"]

#User Id
user_id=1

#Define Functions
def show_skill():
    commit_and_close()

def add_skill():
    skill=input("Write Skill Name: ").strip().capitalize()
    progress=input("Write Skill Progress: ").strip()
    Cr.execute(f"INSERT INTO  skills(name, progress, user_id) values('{skill}','{progress}','{user_id}')")

    commit_and_close()

def delete_skill():
    skill=input("Write Skill Name: ").strip().capitalize()
    Cr.execute(f"DELETE FROM skills WHERE name='{skill}' AND user_id='{user_id}'")
    commit_and_close()

def update_skill():
    commit_and_close()



#Check If Commands Is Exists
if user_input in commands_list:
    print(f"Commands Found {user_input}")

    if user_input =="s":
        show_skill()
    elif user_input =="a":
        add_skill()
    elif user_input =="d":
        delete_skill()
    elif user_input =="u":
        update_skill()
    else:
        print("App Is Closed")

else:
    print(f"Sorry This Commands \"{user_input}\" Is Not Found")