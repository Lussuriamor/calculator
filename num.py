words = ["banana", "apple", "cherry", "grape"]
letter = input("letter:")
for word in words:
    if letter in word:
        print(word)




words = ["banana", "apple", "cherry", "grape", "watermellon"]
longest_word = max(words, key=len)
print(longest_word)




numbers = [1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9]
duplicatenumbers = list(dict.fromkeys(numbers))
print(duplicatenumbers)



sentence = "python is a great programming language"
print(sentence.title())




num = 12345678901234567890
muskednumber = '*' * (len(str(num))-4) + str(num)[-4:]
print(muskednumber)