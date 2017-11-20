# я засмотрелась и случайно сделала ещё несколько вариантов, если вам не трудно - посмотрите, если где ошибки или недоработки
with open("text.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
lines = text.splitlines()
words = text.split()

vsego = 0
stroki = 0


odin = 0 # во сколько раз слов длины 3 больше, чем слов длины 1
tri = 0
for x in words:
    letter = str(x.split())
    dlina = len(letter)-4
    if dlina == 1:
        odin += 1
    if dlina == 3:
        tri += 1
if odin == 0:
    print("Слов длины один нет")
else:
    print("Слов длины три в", int(tri/odin), "раз(а) больше, чем слов длины один")


s_prepinaniem = 0 # какой процент от общего количества слов не оканчивается знаком препинания 
for x in words:
    vsego += 1
    if x[-1] == "," or x[-1] == ".":
        s_prepinaniem += 1
bez_prepinanija = vsego - s_prepinaniem
print(int(bez_prepinanija/vsego*100), "процентов слов не заканчиваются знаком препинания")


longer = 0 # какой процент слов имеет длину больше 10 символов
for x in words:
    vsego += 1
    letter = str(x.split())
    dlina = len(letter)-4
    if dlina > 10:
        longer += 1
print(int(longer/vsego*100), "процентов слов имеют длину больше 10 символов")

big = 0 # какой процент слов начинается с большой буквы;
for x in words:
    vsego += 1
    if x[0].isupper():
        big += 1
print(int(big/vsego*100), "процентов слов начинаются с большой буквы")


n = 0 # какой процент строк содержит больше 5 слов.
for x in lines:
    stroki += 1
    dlina_str = len(x.split())
    if dlina_str > 5:
        n += 1
print(int(n/stroki*100), "процентов строк содержит более 5 слов")
