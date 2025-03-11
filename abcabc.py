from abc import ABC, abstractmethod
class employee(ABC):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    @abstractmethod
    def work(self):
        pass

    def display_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}, зарплата: {self.salary}")

class developer(employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language
    def work(self):
        print(f"{self.name} пишет код на {self.programming_language}")


class manager(employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
    def work(self):
        print(f"{self.name} управляет командой из {self.team_size} человек")

emp1 = developer("Алекс", 30, 70000, "python")
emp2 = manager("Екатерина", 40, 90000, 10)

emp1.display_info()
emp1.work()
emp2.display_info()
emp2.work()

