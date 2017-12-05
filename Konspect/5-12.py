def say_hello(username):
    if len(username) == 0:
        print("hello, anonymus")
        return
    print("hello,", username)

say_hello(input("enter your name: "))

def maximum1(a,b):
    if a > b:
        return a
    else:
        return b

def maximum2(a,b):
    if a > b:
        return a
    return b

print(maximum1(5,2))
print(maximum2(2,5))


def get_syns(target):
    target = target.capitalize()
    with open("syn.txt", encoding="utf-8") as f:
        for line in f:
            splited_line = line.split("#, ")
            word = splited_line[0]
            if word == target:
                syns = splited_line[1]
                syns = syns.strip()
                syns_list = syns.split(', ')
                return(syns_list)

target = input('vvedite slovo: ')
while target != '':
    print(get_syns(target))
    target = input('vvedite slovo: ')


while True:
    target = input('vvedite slovo: ')
    if target == '':
        break
    print(get_syns(target))

