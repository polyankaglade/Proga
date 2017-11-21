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

        
while True:
    line = input('enter smth: ')
    symb = 'a'
    first = line.find(symb)
    
    if line == 'finish':
        break

    if first == -1:
        print('nothing found')
    else:
        second = line[first+1:].find(symb) #можно ещё: second = line.find(symb, first+1)
        if second == -1:
            print('only once')
        else:
            print(second+first+1)
        
