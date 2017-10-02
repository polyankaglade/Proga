# пока не придумала как короче и проще
s = input('Введите слово кириллицей: ')
n = -1
ans = ''
for x in s:
  n += 2
  if n > len(s):
    break
  b = s[n]
  if b == 'а' or b == 'к':
    continue
  ans += b
print('Чётные буквы этого слова, кроме А и К:', ans, end='.')
