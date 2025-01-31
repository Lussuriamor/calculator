decorating = input("Введите тип членства (золото, серебро, обычный):")
sales = float(input("Введите сумму покупки в долларах: "))
if decorating == "золото":
    if sales > 100:
        discount = 0.20
        print("Вы получили 20% скидку, так как ваша покупка больше 100$.")
    else:
        discount = 0.10
        print("Вы получили 10% скидку, так как ваша покупка меньше или равна 100$.")
elif decorating == "серебро":
    if sales > 100:
        discount = 0.15
        print("Вы получили 15% скидку, так как ваша покупка больше 100$.")
    else:
        discount = 0.05
        print("Вы получили 5% скидку, так как ваша покупка меньше или равна 100$.")
elif decorating == "обычный":
    if sales > 100:
        discount = 0.05
        print("Вы получили 5% скидку, так как ваша покупка больше 100$.")
    else:
        discount = 0
        print("Вы не получаете скидки, так как ваша покупка меньше или равна 100$.")
else:
    print("Некорректный тип членства!")
    







salary = float(input("Введите вашу зп в долларах: "))
credit_score = int(input("Введите ваш кредитный рейтинг: "))

if salary > 50000:
    if credit_score > 700:
        print("Кредит одобрен с низкой кредитной ставкой")
    else:
        print("Кредит одобрен с высокой процентной ставкой")
else:
    if credit_score > 500:
        print("Кредит одобрен, но с жесткими условиями")
    else:
        print("Кредит отклонен из-за зарплаты и рейтинга")





number = int(input("Введите число: "))
if number % 4 == 0:
    if number % 2 == 0:
        print("делится на 4 и является четным")
    else:
        print("делится на 4 и является нечетным")
elif number % 5 == 0:
    if number % 2 == 0:
        print("делится на 5 и является четным")
    else:
        print("делится на 5 и является нечетным")
else:
    print("не делится на 4 или 5")



percent=float(input("your percent:"))
hw=str(input("did you done your hw?:"))
if percent >=90:
    hw = input("yes or no")
    if hw == 'yes':
        print("good! A+")
    else:
        print("do your hw! A")
elif percent >=80:
    hw = input("do go to lesson?")
    if hw == 'yes':
        print("good! B+")
    else:
        print("go to lesson!")
else:
    print("work harder!")

