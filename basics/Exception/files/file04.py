FILE = "students.txt"

def add_student(name, age, gpa):
    if age < 0:
        print("🚫 Age cannot be negative")
        return
    if not (0 <= gpa <= 20):
        print("🚫 GPA must be between 0 and 20")
        return
    try:
        with open(FILE, "a", encoding="utf-8") as f:
            f.write(f"{name},{age},{gpa}\n")
    except Exception as e:
        print("⚠ Error writing to file:", e)
    else:
        print("✅ Student added successfully")

def read_students():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("📂 File is empty")
            for line in lines:
                name, age, gpa = line.strip().split(",")
                print(f"👤 {name}, Age {age}, GPA {gpa}")
    except FileNotFoundError:
        print("🚫 File not found. Add some students first.")
    except Exception as e:
        print("⚠ Unexpected error:", e)
    finally:
        print("🔒 Reading process finished")

# ============ Test ============
add_student("Ali", 20, 15.5)
add_student("Sara", 22, 18)
add_student("Omar", -2, 12)  # Invalid age

print("\n📌 Student List:")
read_students()