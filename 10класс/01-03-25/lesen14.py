with open(r'C:\Games\24_9845.txt') as file:
    z = file.readline()
print(z)
x = ""
count = 1
count_max = 0
for i in z:
    if  x in "ABC" and i.isdigit() or x in "89" and i.isalpha():
        count +=1
    else:
        if count_max < count:
            count_max = count
        count = 1
    x = i
    if count_max < count:
        count_max = count
print(count_max)
