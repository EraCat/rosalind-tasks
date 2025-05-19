
ans = 0
l = []
for obj in objects: # доступная переменная objects
    flag = 0
    for e in l:
        if (e is obj):
            flag = 1
            break
    if flag is 0:
        l.append(obj)
        ans+= 1

print(ans)

