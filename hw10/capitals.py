import re
import os
 
 
def open_file():
    text = ""
    correct_input = False
    while not correct_input:
        filename = input("Введите полное название файла: ")
        if os.path.exists(filename):
            correct_input = True
            with open(filename, encoding="utf-8") as f:
                text = f.read()
        else:
            print("Такого файла не нашлось. Попробуйте ещё раз.")
    return text
 
 
def poisk(text):
    result = re.search(">Столица[^А-Яа-я]+?\">?[А-я][а-я]+?\">([А-я][а-я]+?)<",text)
    if result:
        res = result.group(1)
    else:
        res = "не найдена :("
    return res
 
def main():
    print("Столица этой страны - ", poisk(open_file()))
       
main()
