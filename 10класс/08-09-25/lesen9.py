text = list(input())
count = [0 for x in range(128)]

for i in text:
    count[ord(i)] += 1
x = 0
for i in count:
    if i > x:
        x = i
for i in range(128):
    if x == count[i]:
        print(chr(i))
        break

