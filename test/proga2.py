endangered = 0
with open("Extinct_languages.tsv", "r", encoding="utf-8") as f:
    for line in f:
        stroka = line.split("\t")
        if stroka[2] == 'Critically endangered\n':
            endangered += 1
        else:
            continue
print(endangered)
