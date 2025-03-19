# low = input()
# x = ""
# for i in low:
#     if 'A' <= i <= 'Z':
#         o = ord(i)
#         x += chr(o + 32)
#     else:
#         x += i
#
# print(x)
# low = input()
# x= len(low)
# k = 1
# for i in low:
#     if '0' <= i <= "9":
#         print("false")
#         break
#     else:
#         if k == x:
#             print('true')
#         else:
#             k += 1


# text = input()
# x= len(text)
# k = ''
# for i in text:
#     if '0' <= i <= "9":
#        k += i
# print(k)

x = input()
p = 0
o = x.replace("+", " ")
s = ["" for i in range(len(o))]
indexx = 0
for i in o:
    if i == " ":
        indexx += 1
    if "0" <= i <= "9":
        s[indexx] += i

for i in s:
    if i != "":
        p += int(i)
print(s)
print(p)
