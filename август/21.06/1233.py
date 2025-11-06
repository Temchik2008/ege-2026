from re import finditer

# with open('24-334.txt') as file:
#     numbers =  file.readlines()
# pattern = r'([1-9AB][0-9AB]*[02469A])|([1-9AB])'
# matches = [math.group() for match in finditer(pettern, data)]

with open('24-347.txt') as file:
    numbers = file.readline()
pattern = r'[1-7][0-7]*'
matches = [match.group() for match in finditer(pattern, numbers)]
ans = []
for num in matches:
    if int(num, 8) % 13 == 0:

        ans.append(num)
    else:
        for l in range(0, len(num)):
            for r in range(1, len(num) - l):
                num_sliced = num[l:-r]
                if int(num_sliced, 8) %13 == 0:
                    ans.append(num)
                    break
max_num = len(max(ans, key=len))
for num in ans:
    if len(num) == max_num:
        all_max_nums.append(num)
win_num = min(all)

