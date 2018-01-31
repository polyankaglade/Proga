vowels = ["a","e","i","o","u","y"]
qq = 0
word = input("Введите слово на английском: ")
if word == "":
    print("Вы ничего не ввели. Попробуйте ещё раз!")
else:
    for i,n in enumerate(word):
        if n not in vowels:
            continue
        elif n in vowels:
            qq = i
            break
    print(word[qq:]+word[:qq]+"ay")
