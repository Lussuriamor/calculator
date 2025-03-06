class student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
    def display_info(self):
        avg_grade = self.calculate_average()
        print (f"Студент: {self.name}")
        print (f"ID: {self.student_id}")
        print(f" средний балл: {avg_grade}")

student1 = student("Koleso Mashinovich", 101)
student2 = student("Vila Lopatovich", 102)

student1.add_grade (87) 
student2.add_grade (82)

student1.display_info() 
student2.display_info()