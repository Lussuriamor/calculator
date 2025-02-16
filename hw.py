bonus

scores = [85, 72, 33, 68, 47, 95, 80, 77, 49, 89]
ball = ("Балл")
even = 0
odd = 0
for score in scores:
    if score >= 50:
        count = "(сдал)"
    else:
        count = "(не сдал)"
    if score >= 90:
        letter = "Оценка: A"
    elif score >= 80:
        letter = "Оценка B"
    elif score >= 70:
        letter = "Оценка C"
    elif score >= 60:
        letter = "Оценка D"
    else:
        letter = "Оценка F"
    print(f"{ball}: {score} {letter} {count}")



studentscore = [81, 71, 55, 43, 45, 65, 78]
for score in studentscore:
    if score >= 60:
        print("PASS")
    else:
        print("FAIL")




a = [32, 45, 60, 47, 81, 27, 99]
even = 0
odd = 0
for i in a:
    if i % 2==0:
        even +=1
    else:
        odd +=1
print(f'Even: {even}, odd: {odd}')




numbers = [22, 45, 67, 12, 89, 34, 55, 90, 10]
bignum = numbers[0]
smallnum = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > bignum:
        bignum = numbers[i]
    if numbers[i] < smallnum:
        smallnum = numbers[i]
    i += 1

print("Наибольшее число:", bignum)
print("Наименьшее число:", smallnum)





word = input("Your word: ")
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowel = 0
consonant = 0
for letter in word:
    if letter in vowels:
        vowel += 1
    elif letter in consonants:
        consonant += 1

print("lowels:", vowel)
print("Constants:", consonant)

