 # With lets you use a resource(like a file) safly, automatically opening it  at the start and closing it at the end
 #without needing to call close() manually


with open("new.txt","w") as new:
    new.write("hello world!")

with open("messege.txt","r") as m:
    print(m.read())


# Exemple

def add_task(tasku):
    with open("task.txt","a") as task:
        task.write(tasku)

add_task("Learn PYTHON \n")
add_task("Read A Book \n")
add_task("Learn PHP \n")


# Exemple 2
def show_task():
    with open("task.txt","r") as file:
        tasks=file.readlines()
        for i, task in enumerate(tasks ,start=1):
            print(f"{i} {task}")

show_task()