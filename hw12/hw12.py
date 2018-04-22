import os
import re

def makelist():
    make_list = os.listdir('.')
    sort = sorted(make_list)
    dirpath = "."
    result = []
    for x in sort:
        path = os.path.join(dirpath, x)
        if os.path.isdir(path):
           result.append(x)            
    return result

def check_number(spisok):
    n = 0
    result = []
    for x in spisok:
        if re.search("[1-90]",x):
            result.append(x)
            n += 1
        else:
            continue
    print("Всего найдено",n,"папок, содержащих цифры в названии.")
    return result

def print_all(spisok):
    res = []
    for i,x in enumerate(spisok):
        if x not in spisok[:i]:
            res.append(x)
    print("Вот эти папки:")
    for i,x in enumerate(res, start=1):
        print(i,x)

def main():
    print_all(check_number(makelist()))

main()
