from random import randint
n=int(input('Input number: '))
a=[randint(1,11) for i in range(n)]
print(a)
while len(a)<11:
    if len(a)<11:
        a_max=max(a)
        print(a_max)
        break
else:
    print('Input digit less then 10')


