s = input("")
result = ""
for i in s:
    if 'a' <= i <= 'z':
        result += chr(ord(i) - 32)
    else:
        result += i
print(result)