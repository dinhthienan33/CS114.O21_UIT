def main():
    l,r=map(int,input().split())
    print(check(l,r))
def check(l,r):
    password = []
    while(l<=r):
        if(sdb(l)):
            password.append(l)
        l+=1
    return combination(password)      
def combination(factors):
   count=0
   for i in range(len(factors)):
       for j in range(i+1,len(factors)):          
            if(gcd(factors[j],factors[i])==1):
                count+=1
   return count
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def sdb(n):
    for i in range(2,int(n**0.5)+1):
        if n % (i*i)== 0:
            return False
    return True
if __name__ == '__main__':
    main()