numbers = []
x = float(input('enter a number: '))
while x != '':
    numbers.append(x)
    x = input('enter a number: ')
    if x !='':
        x = float(x)
    else:
        break
print(numbers)

n = 0
q = 0
for i in numbers:
    n += i
    q += 1
    
print("Среднее арифметическое = ",n/q)

ind = 0
for i in range(q):
    if numbers[i] > numbers[ind]:
        ind = i    
for i in range(q):
    if numbers[i] == numbers[ind]:
        maximum = numbers[i]

for i in range(q):
    if numbers[i] < numbers[ind]:
        ind = i
for i in range(q):
    if numbers[i] == numbers[ind]:
        minimum = numbers[i]
print("Самое малеьнкое число:",minimum,"\n","Самое большое число:", maximum)
