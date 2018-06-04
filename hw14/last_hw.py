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
            print("Такой файл не найден. Попробуйте ещё раз.")
    return text

def sentences_split(text):
    sen_list = []
    sentences = re.split('[.?!]*[.?!]+?\n*?', text)
    for senten in sentences:
        res = re.sub('[–—,:;«»""“().?!\\n]','',senten)
        sen_list.append(res)
    #print(sen_list)
    return sen_list

def word_len(sentences):
    mydic = {}
    for senten in sentences:
        #print(senten)
        words = re.split("\s",senten)
        for word in words:
            length = len(word)
           # print(word, length)
            if length > 7:
                mydic.update({word:length})
            else:
                continue
    #print(mydic)
    return mydic

def make_table(mydic):
    dlina = max(mydic.values())
    for key,value in mydic.items():
        deff = '-'*(dlina - value)            
        result = '{}{}{:->5}'.format(key,deff,value)
        # в примере для слов длины 8 разное кол-во деффисов
        # в моей штуке оно получается ровное и автоматически подстраивается под максимальную длину слова в тексте
        # сделать автоматическое выравнивание через {:>} у меня не получилось
        # но все условия домашки выполнены - красивая таблица, цифры справа выровнены, метод .формат использован
        print(result)

def main():
    make_table(word_len(sentences_split(open_file())))
                
if __name__ == "__main__":
    main()
