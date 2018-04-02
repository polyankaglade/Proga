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
    return text
 
 
def poisk(text):
    result = re.search(">Столица(?:.)*?title=\"(?:.)*?\">([А-ЯЁ][а-яё]+)",text)
    # >Столица[^А-Яа-я]+?\">?[А-я][а-я]+?\">([А-я][а-я]+?)<
    if result:
        res = result.group(1)
    else:
        res = "не найдено :("
    return res

def write_down(res):
    correct_input = False
    while not correct_input:
        output_file = input("Введите полное название файла, в который следует записать ответ: ")
        if os.path.exists(output_file):
            correct_input = True
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("Столица этой страны - " + res)
        else:
            print("Такой файл не найден. Попробуйте ещё раз.")
    return res
  
def main():    
    print("В файл был записан следующий ответ: ", write_down(poisk(open_file())))
    
       
main()
