s = list(input())
x = s[0]
if 'a' <= x <= 'z':
    s[0] = chr(ord(x) - 32)
for i in range(1, len(s)):
    if 'A' <= str(s[i]) <= 'Z':
        s[i] = chr(ord(s[i]) + 32)
W = ''.join(s)
print (W)