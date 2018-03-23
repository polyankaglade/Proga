import re
def open_file(filename):
    with open(filename,encoding="utf-8") as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    return text

def search(text):
    search_inf = re.findall('[оО]ткрыть[а-я]*[\s,.!?:;]',text)
    search_deeprich = re.findall('[оО]ткрыв[^а]*[\s,.!?:;]',text)
    search_past = re.findall('[оО]ткрыл[а-я]?[\s,.!?:;]',text)
    search_fut = re.findall('[оО]ткро[а-я]*[\s,.!?:;]',text)

    result = []
    result = result + search_inf + search_deeprich + search_past + search_fut
    return result

def clean_results(result):
    spisok = []
    for i in result:
       i = i.strip()
       punct = re.findall('[\s,.!?:;]',i)
       for x in punct:
           i = i.replace(x,'')
       spisok.append(i)
    return spisok

def check(formy):
    final_results = []
    for i,s in enumerate(formy):
        if s in formy[:i]:
            continue
        else:
            final_results.append(s)
    return final_results

def main_func():
    filename = input("Введите полное название файла")
    main_res = check(clean_results(search(open_file(filename))))
    print("В данном тексте встретились следующие формы глагола \'открыть\':")
    for i in main_res:
        print(i)

main_func()
