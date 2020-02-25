from random import randint

a1 = [randint(1, 11) for i in range(1, 11)]
a2 = [randint(1, 11) for i in range(1, 11)]
a3 = []
print(a1)
print(a2)
while len(a1)>0 and len(a2)>0:
    for g in a1:
        if g in a3:
            continue
        for j in a2:
            if g == j:
                a3.append(g)
                break
    print(a3)
    break