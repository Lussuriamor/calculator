def calculator():
    print("Выберите операцию")
    print("1/ +")
    print("2/ -")
    print("3/ *")
    print("4/ %")
    print("5/ sqrt")
    print("6/ pow")
    print("7/ pow3")
    print("8/ /")

    choice = input("Введите номер операции (1.2.3.4.5): ")

    num1 = float(input("Введите первое число"))
    num2 = float(input("Введите второе число"))

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        print((num1 * num2)/100)
    elif choice == '5':
        sqrt = num1 ** (0.5)
        print(sqrt)
    elif choice == '6':
        result = (num1 ** num2)
        print(result)
    elif choice == '7':
        result = (num1**3)
        print(result)
    elif choice == '8':
        if num2 !=0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Ошибка! Деление на ноль.")
    else:
        print("Неверный ввод!")

if __name__ == "__main__":
    calculator()


weight = float(input("ваш вес:"))
hight = float(input("ваш рост:"))
bmi = weight/(hight/100)**2
print(bmi)
if bmi <18.5:
    print("ниже обычного")
elif bmi <24.9:
    print("нормальный")
elif bmi <29.9:
    print("выше обычного")
elif bmi <34.9:
    print("на грани ожирения")
else:
    print("ОЖИРЕНИЕ")



def mark(percent):
    if percent >=90:
        return 'A'
    elif percent >= 75:
        return 'B'  
    elif percent >= 65:
        return 'C'  
    elif percent >= 50:
        return 'D'  
    else:
        return 'F'  
percent = float(input("ваш процент?: "))
grade = mark(percent)
print(f"Ваша оценка: {grade}")




import random

def gameofnumbers():
    
    numbergame = random.randint(1, 100)

    print("Угадай число от 1 до 100:")

    while True:
        guess = float(input("Гадай: "))

        if guess == numbergame:
            print(f"КРАСАВЧИК! {numbergame}!")
            break
        elif abs(numbergame - guess) <= 10:
            print("Горячо!")
        elif abs(numbergame - guess) <= 20:
            print("Тепло!")
        else:
            print("Холодно!")

gameofnumbers()