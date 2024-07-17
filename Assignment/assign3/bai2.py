import sys
import time

def main():
    n = int(sys.stdin.readline())
    arr_n = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    arr_m = list(map(int, sys.stdin.readline().split()))
    start_time=time.time()
    for i in range(m):
        x=search(arr_n,arr_m[i])
        if(x!=-1):
            print(x)
        else:
            print(-1)
    print(time.time()-start_time)
def search(arr,x):
    l,r=0,len(arr)-1
    while (l<r):
        mid=(l+r)//2
        if(arr[mid]<x):
            l=mid+1
        else:
            r=mid
    if(arr[l]==x):
        return l
    return -1
    
    
if __name__ == '__main__':
    main()