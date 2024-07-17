import math
def solve(n):
    count = 0
    h=int(n /1.4)+1
    np=pow(n,2)
    for i in range(1,h):
        k=math.sqrt(np - pow(i,2))
        if int(k)==k:
            count += 1
    return count

n = int(input())
result = solve(n)
print(result)