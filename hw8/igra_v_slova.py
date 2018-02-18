import random
def create_dic(filename):
    mydic = {}
    
    with open (filename, encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n","")
            slovo,podskazka = line.split(',') #в файле слова записаны по типу слово,подсказка
            mydic[slovo]=podskazka
    return mydic

def soglasie():
    answer = input("Хочешь сыграть ещё? (да/нет)")
    while answer == "":
        print("Ты ничего не ввел, ответь ещё раз.")
        answer = input("Хочешь сыграть ещё? (да/нет)")
    return answer

def uslovie(dictionary):
    target = random.choice(list(dictionary.keys()))

    show_user = ''
    show_user = show_user + dictionary[target] + " "
    for letter in target: #кажется это заодно задание второго варианта, я случайно его сделала
        show_user += "."
    print("Загадано слово(каждая буква заменена точкой):",show_user)

    return target

def igra(target,score): #я для красоты сделала счётчик угаданых слов
    popytka = len(target)
    print("Всего у тебя",popytka,"попыток.\n") #я не поняла надо ли сообщать сколько попыток, так что решила сообщить
    while 0 < popytka <= len(target):
        guess = input("Какое слово загадано? ")
        if guess == target:
            print("Ура, это правильный ответ!\n")
            score += 1
            break
        elif guess == "":
            print("Ты ничего не ввел!")
            continue
        else:
            popytka += -1
            print("Нет, это не правильный ответ. У тебя ещё",popytka,"попыток.")

    if popytka == 0:
        print("К сожалению тебе не удалось отгадать слово :(\n")
    return score

def game():
    dictionary = create_dic("igra.csv")
    score = 0
    answer = "да"
    while answer == "да":
        score = igra(uslovie(dictionary),score)
        answer = soglasie()
    print("Спасибо за игру! Твой счёт:", score)
    
game()
