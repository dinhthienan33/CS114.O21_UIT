import math
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def main():
    l,r =map(int,input().split())
    numbers = [i for i in range(l, r + 1)]
    n=l-r+1
    for j in range(len(numbers)):
        if(sdb(numbers[j]) ==False):
            numbers.pop(j)
    count=0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if gcd(numbers[i],numbers[j])==1: 
                count += 1           
    print(numbers)
def sdb(n):
    for u in range(2, math.isqrt(n) + 1,u*u):
        if n % (u ** 2) == 0:
            return False
    return True
if __name__ == '__main__':
    main()