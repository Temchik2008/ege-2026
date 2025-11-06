full_n = []
for n in range(0, 10000):

    n = bin(n)[2:]
    if int(n)%3 == 0:
        r = n + n[-3:]
    else:
        r = n + bin((int(n)%3)*3)[2:]

    if int(r, base=2) < 130:
        full_n.append(int(n, base=2))
    else:
        print(max(full_n))







