import random
mydic = {}
with open ("igra.csv", encoding="utf-8") as f:
    for line in f:
        line = line.replace("\n","")
        slovo,podskazka = line.split(',') #в файле слова записаны по типу слово,подсказка
        mydic[slovo]=podskazka
user_answer = "да"
while user_answer == "да":
    target = random.choice(list(mydic.keys()))

    show_user = ''
    show_user = show_user + mydic[target] + " "
    for letter in target:
        show_user += "."
    print("Загадано слово(каждая буква заменена точкой):",show_user)

    popytka = len(target)
    print("Всего у тебя",popytka,"попыток")

    for i in range(len(target)):
        guess = input("Какое слово загадано? ")
        if guess == target:
            print("Ура, это правильный ответ!")
            break
        elif guess == "":
            print("Ты ничего не ввел!")
            continue
        else:
            popytka += -1
            print("Нет, это не правильный ответ. У тебя ещё",popytka,"попыток")

    if popytka == 0:
        print("К сожалению тебе не удалось отгадать слово :(")
    user_answer = input("Хочешь сыграть ещё? (да/нет)")
print("Спасибо за игру!")
