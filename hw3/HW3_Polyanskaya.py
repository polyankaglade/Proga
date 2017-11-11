request = str(input('Введите слово: '))
n = -1
print(request)
for x in request:
    result = request[:n]
    print(result)
    n -= 1
