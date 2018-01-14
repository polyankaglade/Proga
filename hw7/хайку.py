#сначала открываем кучу файлов со словами и записываем их списками в переменные
with open("one_part.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
one_part = text.split()

with open("one_noun_sg.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
one_noun_sg = text.split()

with open("one_noun_pl.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
one_noun_pl = text.split()

with open("two_adj_sg.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
two_adj_sg = text.split()    

with open("three_adj_sg.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
three_adj_sg = text.split()

with open("two_adj_pl.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
two_adj_pl = text.split()

with open("three_adj_pl.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
three_adj_pl = text.split()

with open("two_noun_sg.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
two_noun_sg = text.split()

with open("two_noun_pl.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
two_noun_pl = text.split()

with open("three_noun_sg.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
three_noun_sg = text.split()

with open("three_noun_pl.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
three_noun_pl = text.split()

with open("two_verb_sg.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
two_verb_sg = text.split()

with open("two_verb_pl.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
two_verb_pl = text.split()

with open("three_verb_sg.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
three_verb_sg = text.split()

with open("three_verb_pl.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
three_verb_pl = text.split()

import random
number = 0 #обнуляем переменную, она используется для согласования первой и второй строчки по числу (ну просто по приколу)

punct = [".",",","...","!","?"," -"]
#начинаем определять функции
#сначала идут группы по пять слогов из двух и трёхсложных существительных и прилагательных
#отдельно для единственного числа
def five_noun_group_sg():
    sluch = random.choice([1,2,3,4]) #для случайного выбора порядка слов
    number = 1
    
    if sluch == 1:
        return random.choice(two_adj_sg)+ " " + random.choice(three_noun_sg)
    elif sluch == 2:
        return random.choice(three_adj_sg)+ " " + random.choice(two_noun_sg)
    elif sluch == 3:
        return random.choice(three_noun_sg)+ " " + random.choice(two_adj_sg)
    elif sluch == 4:
        return random.choice(two_noun_sg)+ " " + random.choice(three_adj_sg)

#отдельно для множественного числа 
def five_noun_group_pl():
    sluch = random.choice([1,2,3,4])
    number = 2
    
    if sluch == 1:
        return random.choice(two_adj_pl)+ " " + random.choice(three_noun_pl)
    elif sluch == 2:
        return random.choice(three_adj_pl)+ " " + random.choice(two_noun_pl)
    elif sluch == 3:
        return random.choice(three_noun_pl)+ " " + random.choice(two_adj_pl)
    elif sluch == 4:
        return random.choice(two_noun_pl)+ " " + random.choice(three_adj_pl)

#далее идут группы того же типа, но с глаголом вместо прилагательного
def five_verb_group_sg():
    sluch = random.choice([1,2,3,4])
    numver = 1
    
    if sluch == 1:
        return random.choice(two_verb_sg)+ " " + random.choice(three_noun_sg)
    elif sluch == 2:
        return random.choice(three_noun_sg)+ " " + random.choice(two_verb_sg)
    elif sluch == 3:
        return random.choice(three_verb_sg)+ " " + random.choice(two_noun_sg)
    else:
        return random.choice(two_noun_sg)+ " " + random.choice(three_verb_sg)


def five_verb_group_pl():
    sluch = random.choice([1,2,3,4])
    number = 2
    
    if sluch == 1:
        return random.choice(two_verb_pl)+ " " + random.choice(three_noun_pl)
    elif sluch == 2:
        return random.choice(three_noun_pl)+ " " + random.choice(two_verb_pl)
    elif sluch == 3:
        return random.choice(three_verb_pl)+ " " + random.choice(two_noun_pl)
    else:
        return random.choice(two_noun_pl)+ " " + random.choice(three_verb_pl)

#это функции для составления второй строчки, из семи слогов
#(гл+сущ+прил)
def seven_group_threewords():
    if number == 1:
        return random.choice(two_verb_sg)+ " " + five_noun_group_sg()
    else:
        return random.choice(two_verb_pl)+ " " + five_noun_group_pl()

#гл+частица\слово+прил+сущ
def seven_group_fourwords():
    if number == 1:
        return random.choice(two_verb_sg)+ " " + random.choice(one_part)+" " + random.choice(two_adj_sg)+ " " + random.choice(two_noun_sg)
    else:
        return random.choice(two_verb_pl)+ " " + random.choice(one_part)+" " + random.choice(two_adj_pl)+ " " + random.choice(two_noun_pl)

#гл+сущ прил+сущ
def seven_group_fourwords_comma():
    if number == 1:
        return random.choice(two_verb_sg)+ " " + random.choice(one_noun_sg)+ random.choice(punct) +" " + random.choice(two_adj_sg)+ " " + random.choice(two_noun_sg)
    else:
        return random.choice(two_verb_pl)+ " " + random.choice(one_noun_pl)+ random.choice(punct) +" " + random.choice(two_adj_pl)+ " " + random.choice(two_noun_pl)

#тут случайный выбор группы из пяти слогов
def choose_five():
    sluch = random.choice([1,2,3,4])
    if sluch == 1:
        return five_noun_group_sg()
    elif sluch == 2:
        return five_noun_group_pl()
    elif sluch == 3:
        return five_verb_group_sg()
    elif sluch == 4:
        return five_verb_group_pl()

#тут случайный выбор строчки из семи слогов
def choose_seven():
    sluch = random.choice([1,2,3,4])
    if sluch == 1:
        return seven_group_threewords()
    elif sluch == 2:
        return seven_group_fourwords()
    elif sluch == 3:
        return seven_group_fourwords_comma()

#финальный код котрый собирает хайку
def create_poem():
    print(choose_five() +random.choice(punct))
    print(choose_seven() +random.choice(punct)) #иногда питон выдает ошибку вот тут, но если удалить/добавить пробел после плюса оно нормально работает
    print(choose_five() +random.choice([".","!","?",]))
    

create_poem()

