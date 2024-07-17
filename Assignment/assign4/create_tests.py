import random as rd
n=int(input())
row=[]
for _ in range(n):
    row.append([rd.randint(1, 2), rd.randint(0,1000000)])
with open('test_cases.txt', 'w') as f:
    for r in row:
        f.write(' '.join(str(num) for num in r)+'\n')
    f.close()