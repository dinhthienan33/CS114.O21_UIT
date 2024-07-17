from bisect import insort
import sys
from sys import stdin,stdout
import time as t

def main():
    arr=[]
    result=[]
    with open('test_cases.txt', 'r') as rf:
        lines=rf.readlines()
        rf.close()
    start=t.time()
    result=[]
    for line in lines:
            a,b=line.split() 
            a=int(a)
            b=int(b)          
            if(a==1):
                if(binary_search(arr,b)==-1):
                    insort(arr,b)
            if(a==2):
                index=binary_search(arr,b)
                result.append(index+1)
    with open('output.txt', 'w') as wf:
        for x in result:
            wf.write(str(x)+'\n')
        wf.close()
    end=t.time()
    print(end-start)
    
def binary_search(arr,x):
    l,h=0,len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid] ==x):
            return mid
        if(arr[mid]<x):
            l=mid+1
        else:
            h=mid-1
    return -1
if __name__ == '__main__':
    main()