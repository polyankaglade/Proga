vowels = ["а","е","ё","и","о","у","ы","э","ю","я"]

word = str(input("Введите слово: "))
new = ''

for i in word:
    if i in vowels:
         new = new +i+"с"+i
    else:
        new += i

print(new)
