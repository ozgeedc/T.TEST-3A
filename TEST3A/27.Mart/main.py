

# Clear the screen
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

import student
import teacher

def commands_info(raw_cmd , flag):
    if flag:
        print(f"Commands '{raw_cmd}' not faund.")
    print(f"""Commands:
    add    - Add a student
    remove - Remove a student
    list   - List students
    clear  - Clear the screen
    exit   - Exit the program""")
clear()
commands_info("", False)
_student = student.Student()
_teacher = teacher.Teacher()
while True:
    try:
        raw_cmd = input(f"> ")
        cmd = raw_cmd.strip().lower()
        if not cmd:
            continue
        elif cmd == "exit":
            print(f"Exited by user.")
            break

        elif cmd == "clear":
            clear()

        elif cmd == "add":
            choice = input(f"\t\b\bAdd a student or teacher? (s/t): ").strip().lower()
            if choice == "s":
                First_name = input(f"\tFirst name:")
                Last_name = input(f"\tLast name:")
                Gender = input(f"\tGender: ")
                Number = int(input(f"\tNumber(int):"))
                _student.add(First_name, Last_name, Gender, Number)
            elif choice == "t":
                First_name = input(f"\tFirst name:")
                Last_name = input(f"\tLast name:")
                Gender = input(f"\tGender: ")
                Branch = input(f"\tBranch: ")
                _teacher.add(First_name, Last_name, Gender, Branch)
            else:
                print(f"Invalid choice.")

        elif cmd == "remove":
            choice = input(f"\t\b\bAdd a student or teacher? (s/t):").strip().lower()
            if choice == "s":
                Number = int(input(f"\tStudent number(int): "))
                _student.remove(Number)
            elif choice == "t":
                First_name = input(f"\tFirst_name: ")
                Last_name = input(f"\tLast_name: ")
                _teacher.remove(First_name + " " + Last_name)
            else:
                print(f"Invalid choice.")

        elif cmd == "list":
            choice = input(f"\t\b\bList students or teachers? (s/t): ").strip().lower()
            if choice == "s":
                _student.list(_student.student_list)
            elif choice == "t":
                _teacher.list(_teacher.teacher_list)
            else:
                print(f"Invalid choice.")

        else:
            commands_info(raw_cmd, True)
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print(f"\nExited by user.")
        break