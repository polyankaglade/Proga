# первый вариант
# чему равно среднее число слов в строке
with open("text.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
lines = text.splitlines()

stroki = 0
vsego = 0
for x in lines:
    stroki += 1
    dlina_str = len(x.split())
    vsego += dlina_str
print("Средняя длина строки: ", int(vsego/stroki))
