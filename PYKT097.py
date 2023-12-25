import re
a = []
while True:
    try:
        s = input()
        if s == "": break
        b = re.split(r'(?<=[.!?])\s', s)
        for i in b:
            if i != "":
                tmp = ' '.join(i.strip().split()).lower()
                tmp = tmp[:1].upper() + tmp[1:]
                if tmp[-1] not in [".", "?", "!"]: tmp += "."
                if tmp[-2] == " ": tmp = tmp[:-2] + tmp[-1]
                a.append(tmp)
    except:
        break

for i in a:
    print(i)
    
    


    