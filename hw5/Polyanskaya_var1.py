# удаляет третью букву из оргинального слова, а не из перевернутого
print('when done writing, just press ENTER for programm to calculate the results')
with open("text.txt", "w", encoding="utf-8") as f:
    x = input('enter a latin verb: ')   
    while x != '':
        y = ' '
        word = ''
        reversed_word = ''
        y += x
        for i,a in enumerate(y):
            if i%3 == 0:
                continue
            word +=(y[i])
        z = ' ' + word
        for s,o in enumerate(z):
            reversed_word +=(z[-s])
        x = input('enter a latin verb: ')
        f.write(reversed_word[1:] + '\n')
