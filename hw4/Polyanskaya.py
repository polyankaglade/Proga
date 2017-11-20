# первый вариант
vsego = 0
stroki = 0

for x in lines: # чему равно среднее число слов в строке
    stroki += 1
    dlina_str = len(x.split())
    vsego += dlina_str
print("Средняя длина строки: ", int(vsego/stroki))
