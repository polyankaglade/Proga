line = input()
# loHel
half_ind = (len(line)+1)//2
print(half_ind)
new_line = line[half_ind:] + line[:half_ind]
print(new_line)


while True:
    line = input('enter smth: ')
    symb = 'a'
    first = line.find(symb)
    last = line.rfind(symb)
    if line == 'finish':
        break

    if first == -1:
        print('nothing found')
    elif first == last:
        print('one time, number', first)
    else:
        print('first:',first, 'last:', last)
