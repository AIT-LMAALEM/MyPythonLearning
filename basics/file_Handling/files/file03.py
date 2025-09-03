# Simple Note-taking Project

def add_note(note):
    """Add a new note to the file"""
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

def show_notes():
    """Read and display all notes"""
    with open("notes.txt", "r") as file:
        notes = file.readlines()
        if not notes:
            print("No notes found.")
        else:
            print("Your Notes:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")

while True:
    print("\n1. Add Note")
    print("2. Show Notes")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Enter your note: ")
        add_note(note)
    elif choice == "2":
        show_notes()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")