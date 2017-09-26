# 1
for i in range(1, 30, 2):
    print (i)

# 2 
i = 9
while i >= 5:
    print(i)
    i -= 1
   
# 3
# шифр Цезаря
shifr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяаб   '
a = input('введите предложение кириллицей без заглавных букв')
ans = ''
for x in a :
    b = shifr.find(x)
    c = shifr[b+2]
    ans += c
print(ans)
