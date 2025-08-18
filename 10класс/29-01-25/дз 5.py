base = int(input())
num = int(input())
res = ""
if not (2 <= base <= 9):
    print("ошибочка. читать научись")
else:
    while num:
        res += str(num % base)
        num //= base
print("".join(list(reversed(res))))