with open("text.txt", "w", encoding="utf-8") as f:
    x = ' '   
    while x != '':
        y = ' '
        word = ''
        x = input('enter a latin verb')
        y += x
        for i,res in enumerate(y):
            word +=(y[-i])
        result = word[1:]
        f.write(result + '\n')
