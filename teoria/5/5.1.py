for n in range(1, 1000):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '0'

    else:
        r = '11' + r[2:] + '1'

    if int(r, base=2) >= 16:
        print(n)
        break