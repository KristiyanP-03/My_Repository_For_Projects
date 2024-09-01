# zad 1
# a = int(input())
# b = int(input())
#
# volume = a * b
#
# print(f"Въведете дължината на правоъгълника: {a}")
# print(f"Въведете широчината на правоъгълника: {b}")
# print(f"Лицето на правоъгълника е: {volume}")



# zad 2
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

student1 = Student("Кристиян Красимиров Писев", 3.0)


command_list = ["add", "delete", "listAll"]
object_list = [student1]
while(True):
    command_line = input()

    command_parts = command_line.split()

    command = command_parts[0]

    if command not in command_list:
        print("Error! Command not existing!")
        break

    if command == "add":
        name = command_parts[1]
        grade = command_parts[2]
        object_list.append(Student(name, grade))

    elif command == "delete":
        name = command_parts[1]

        for student in object_list:
            if student.name == name:
                object_list.remove(student)
                print(f"Student {name} removed.")
                break
        else:
            print("Student not found")


    elif command == "listAll":
        for student in object_list:
            print(
                f"Name: {student.name}, Grade: {student.grade}"
            )
