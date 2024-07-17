import sys
def main():
    n = int(sys.stdin.readline())
    arr_n = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    arr_m = list(map(int, sys.stdin.readline().split()))
    arr_n.reverse()
    for i in range(m):
        x=search(arr_n,arr_m[i])
        if(x!=-1):
            print(n-x-1)
        else:
            print(-1)
        
def search(arr,x):
    l,r=0,len(arr)-1
    if(l==r):
        return l
    while (l<r):
        mid=(l+r)//2
        if(arr[mid]>x):
            l=mid+1
        else:
            r=mid
    if(arr[l]==x):
        return l
    return -1
    
    
if __name__ == '__main__':
    main()