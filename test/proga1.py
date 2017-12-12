with open("Extinct_languages.tsv", "r", encoding="utf-8") as f:
    for line in f:
        dlina = len(line)
        if dlina > 35:
            print(line)
        else:
            continue
    
       
