n = 0
result = ''
not_found = ''
x = input('enter a name of a language')
with open("Extinct_languages.tsv", "r", encoding="utf-8") as f:
    
    while x != '':
        x = x.capitalize()
        for line in f:
            stroka = line.split("\t")
            
            if x in line:
                info = str(stroka[0]+'-'+stroka[1]+'-'+ stroka[2])               
                result += info
                n += 1                
                break
            else:
                n = 0
                continue
        if n == 0:
            not_found += '\"'+x+'\"'+' '
        x = input('enter a name of a language')
    
    if n == 0:
        print(result, not_found + "- not on the list")
    else:
        print(result)
