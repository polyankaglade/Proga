def file_read():
    filename = input("Введите название файлв (без .txt): ")
    filename += ".txt"
    try:
        f = open(filename)
    except IOError as e:
        print("Не удалось найти этот файл. Попробуйте ещё раз.")
    else:  
        with open(filename, encoding="utf-8") as f:
            text = f.read()
        words_raw = text.split()
        words = []
        for word in words_raw:
            word = word.strip(".,!?:;\n")
            words.append(word)
        return words

def count_ing(words):
    ings = 0
    for word in words:
        if word[-3:] == "ing":
                ings += 1   
    print("Всего в тексте",ings,"форм на -ing.")
    
def find_ing(words):
        find_word = input("Введите слово на -ing для поиска по тексту: ")
        found_word = 0
        if find_word[-3:] == "ing":
            for word in words:
                if word == find_word:
                    found_word += 1
        if found_word == 0:
            print("Ничего не найдено. Попробуйте изменить запрос.")
        else:
            print("Слово",find_word,"встречается",found_word,"раз(а).")   

def ing_info():
    words = file_read()
    count_ing(words)
    find_ing(words)

ing_info()
