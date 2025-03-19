# with open(r'C:\Games\24_9845.txt') as file:
#     x = file.readline()
# count = 1
# count_max = 0
# a = 'EYUIOA'
# b = 'QWRTPSDFGHJKLZXCVBNM'
# for i in range(1, len(x)):
#     if (x[i-1] in a and x[i] in b) or (x[i-1] in b and x[i] in a):
#         count += 1
#     else:
#         count = 1
#     if count_max < count:
#         count_max = count
# print(count_max)

# x = 'HEFYWGUQISJAXNDVHBFGREYUEWSADIJCNHBFGRYUEFRIWJQSAKMCNDHSVY'
# count = 1
# count_max = 0
# a = 'EYUIOA'
# b = 'QWRTPSDFGHJKLZXCVBNM'
# for i in a:
#     x = x.replace(i, '1')
# for i in b:
#     x = x.replace(i, '0')
# x = x.replace("11", '1 1')
# x = x.replace("00", '0 0')
# x = x.replace("11", '1 1')
# x = x.replace("00", '0 0')
# x = x.split()
# print(len(max(x, key=len)))

x = 'KKKAXMMKKKAXMM'
count = 3
count_max=0
for i in range(len(x)-3):
    if x[i] == 'A' and x[i+1] == "X" and x[i+2] == "M" and x[i+3] == "M":
        count = 3
    else:
        count += 1
    if count_max < count:
        count_max = count
print(count_max)

