# вариант №1
x = list(input('enter a word: '))
x +=''.join(' ')
# я не понимаю как добиться чтоб i было 0 при первом прогоне
for i,result in enumerate(x):
    result = ''.join(x[:-i])
    print(result)

