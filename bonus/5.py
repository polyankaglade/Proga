cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]

word = str(input("Введите слово или фразу (на английском): "))
new = ""
if word == "":
    print("Вы ввели пустую строку, попробуйте ещё раз!")
else:
    for i in word:
        if i in cons:
            new = new + i + "aig"
        else:
            new += i
        print(new)
