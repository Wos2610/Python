with open('DATA.in', 'wb') as f:
    b = ["AAA", "BBB"]
    f.write(b[0].encode('utf-8'))

with open('DATA.in', 'rb') as f:
    a = f.read()
    print(a.decode('utf-8'))

