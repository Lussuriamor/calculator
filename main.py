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