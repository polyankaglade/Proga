line = input()
# loHel
half_ind = (len(line)+1)//2
print(half_ind)
new_line = line[half_ind:] + line[:half_ind]
print(new_line)
