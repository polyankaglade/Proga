while True:
    a = int(input('Введите год: '))
    if a == 0:
        print('Error') 
    elif (not a%100 == 0 and a%4 == 0) or a%400 ==0:
        print('YES')
    else:
        print('NO')
