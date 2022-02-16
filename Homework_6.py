list = [1, 2, 3, 4, 5, 6, 7] # input list here
k = 3 # input index here
for i in range(len(list)):
    if i < k:
        continue
    elif i < len(list) - 1:
        list[i] = list[i + 1]
    else:
        list.pop()
print(list)