def gcd(a, b):
    while b: a, b = b, a % b
    return a

def main():
    l,r = map(int,input().split())
    numbers = [True]*(r-l+1)
    count = 0
    
    special_number=[]
    checksdb(numbers,l,r)
    for i in range(l, r+1):
        if numbers[i-l]: 
            special_number.append(i)
    for i in range(len(special_number)):
        for j in range(i+1, len(special_number)):
            if gcd(special_number[i],special_number[j])==1: 
                count += 1
                
    print(count)

def checksdb(numbers,l,r):
    for i in range(2, int(math.sqrt(r)) + 1):
        start = math.ceil(l/(i*i))*pow(i,2)
        for j in range(start, r+1, i*i):
            numbers[j-l]=False
    return numbers
if __name__ == "__main__":
    main()