import sqlite3
import os
import time

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
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")
    
def show_skill():
    clear_screen()
    Cr.execute(f"SELECT * FROM skills WHERE user_id='{user_id}'")
    results=Cr.fetchall()
    print(f"You Have {len(results)}")
    if len(results)>0:
        print("Showing Skills With Progress")
        time.sleep(1)
        for row in results:
            print(f" Skill => {row[0]},",end=" ")
            print(f" Progress => {row[1]}")
    commit_and_close()


def add_skill():
    clear_screen()
    skill=input("Write Skill Name: ").strip().capitalize()
    Cr.execute(f"SELECT name FROM skills WHERE name='{skill}' AND user_id='{user_id}'")
    results=Cr.fetchone()
    if results !=None:
        print("Skill Is Exists you Can't Add It")
    else:
        progress=input("Write Skill Progress: ").strip()
        Cr.execute(f"INSERT INTO  skills(name, progress, user_id) values('{skill}','{progress}','{user_id}')")
        time.sleep(1)
        print("Skill Is Added ")
    commit_and_close()


def delete_skill():
    clear_screen()
    skill=input("Write Skill Name: ").strip().capitalize()
    Cr.execute(f"DELETE FROM skills WHERE name='{skill}' AND user_id='{user_id}'")
    time.sleep(1)
    print("Skill Is Deleted")
    commit_and_close()


def update_skill():
    clear_screen()
    skill=input("Write Skill Name: ").strip().capitalize()
    new_progress=input("Write The New Progress").strip()
    Cr.execute(f"UPDATE skills SET progress ='{new_progress} WHERE user_id='{user_id}' AND name='{skill}'")
    time.sleep(1)
    print("Skill Is Updated")
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

















