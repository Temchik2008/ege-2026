#система счисления
n = 25
print(bin(n)[2:])
print(f'{n:b}') #oct hex o x
#перевод в любую систему от 2 до 9
def convert(num):
    res = ''
    while num:
        res += str(num%3)
        num //=3
    return res[::-1]

from string import digits, ascii_lowercase
#перевод в любую систему от 2 до 36
def convert(num):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //=3
    return res[::-1]

bin_num = '101'
oct_num = '765'
tri_num = '1201'