import re

def open_file():
    with open ("mystem.xml", encoding="utf-8") as f:
        text = f.read()
    return text

def search(text):
    result = re.findall("<w><ana lex=\"(?:.)*?\" gr=\"(.*?)\"",text)
    return result

def create_dic(gram):
    dic = {}
    for i in gram:
        n = 0
        for x in gram:
            if i == x:
                n += 1
            else:
                continue
        s = {i:n}
        dic.update(s)
    return dic
            
def write_results(dic):
    
    with open("result.txt","w", encoding="utf-8") as f:
        for i in dic:
            f.write(i+"\n")
    return f

def main():
    write_results(create_dic(search(open_file())))
    print("done")

main()
