num = int(input())
sys = 7

res = ""
while num:
    res += str(num % sys)
    num //= sys
print ("".join(list(reversed(res))))