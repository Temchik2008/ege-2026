x =input()
x = x.split()
xo = 0
for i in x:
    if i.count('-')%2:
        xo +=1
print(xo)


