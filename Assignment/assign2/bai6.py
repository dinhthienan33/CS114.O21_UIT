def main():
    n=int(input())
    arr=[]
    for _ in range(n):
        k=int(input())
        arr.append(k)
    arr.sort()
    count=0
    for i in range(1,n):
        if(arr[i]-arr[i-1]!=1):
            count+=arr[i]-arr[i-1]-1       
    print(count)
if __name__ == '__main__':
    main()
    