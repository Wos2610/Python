import re
str = ""
a = []
while True:
    try:
        str += input()
    except EOFError:
        break
str = str.strip()
a = re.split('[.!?]', str)

for i in range(len(a)):
    a[i] = a[i].strip().lower()
    a[i] = re.sub(" +"," ",a[i])
    a[i] = a[i][:1].upper() + a[i][1:]
    print(a[i])