from student import Student
from file_manager import save_students, load_students

def display_menu():
    print("Меню:")
    print("1. Добавить студента")
    print("2. Просмотреть студентов")
    print("3. Удалить студента по ID")
    print("4. Сохранить и выйти")
    print("5. Выйти без сохранения")

def add_student():
    student_id = input("Введите ID студента: ")
    name = input("Введите имя студента: ")
    age = int(input("Введите возраст студента: "))
    grade = input("Введите оценку студента: ")
    return Student(student_id, name, age, grade)

def view_students(students):
    if students:
        print("Список студентов:")
        for student in students:
            print(student)
    else:
        print("Студенты не найдены.")

def delete_student_by_id(students, student_id):
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print(f"Студент с ID {student_id} удален.")
            return True
    print(f"Студент с ID {student_id} не найден.")
    return False

def main():
    students = load_students()
    
    while True:
        display_menu()
        choice = input("Выберите опцию (1-5): ")

        if choice == '1':
            student = add_student()
            students.append(student)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            view_students(students)
            student_id = input("Введите ID студента для удаления: ")
            delete_student_by_id(students, student_id)
        elif choice == '4':
            save_students(students)
            print("Данные сохранены.")
            break
        elif choice == '5':
            print("Выход без сохранения.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()