import json
from student import Student

FILE_NAME = "students.json"

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json_data = [student.__dict__ for student in students]
        json.dump(json_data, file, ensure_ascii=False, indent=4)

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            students_data = json.load(file)
            return [Student(**data) for data in students_data]
    except FileNotFoundError:
        return []