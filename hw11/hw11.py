import re
import os

def open_file():
    text = ""
    correct_input = False
    while not correct_input:
        filename = input("Введите полное название файла с html кодом: ")
        if os.path.exists(filename):
            correct_input = True
            with open(filename, encoding="utf-8") as f:
                text = f.read()
        else:
            print("Такой файл не найден. Попробуйте ещё раз.")
    #print(text)
    return text

def change(text):
    result1 = re.sub("[^а-яА-я]?(комар)[^а-яА-я]","слон",text)
    result2 = re.sub("[^а-яА-я]?(Комар)[^а-яА-я]","Слон",text)
    print(result1, result2)
    return result2

def write_down(result):
    text = ""
    correct_input = False
    while not correct_input:
        filename = input("Введите полное название файла, куда записать текст: ")
        if os.path.exists(filename):
            correct_input = True
            with open(filename,"w", encoding="utf-8") as f:
                text = f.write(result)
        else:
            print("Такой файл не найден. Попробуйте ещё раз.")
    return text

def main():
    write_down(change(open_file()))
    

main()
