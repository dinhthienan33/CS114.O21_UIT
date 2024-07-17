from bisect import insort,bisect_left
from sys import stdin,stdout
def main():
    ip=input()
    arr=[]
    while(ip!='0'):
        a,b=map(int,ip.split())
        if(a==1) and (binary_search(arr,b)==-1) :
            insort(arr,b)
        if(a==2):
            print(binary_search(arr,b)+1)
        ip=input()
def binary_search(a, x):
    low=0
    high=len(a)
    pos =bisect_left(a, x, low, high)             
    return pos if pos != high and a[pos] == x else -1
if __name__ == '__main__':
    main()