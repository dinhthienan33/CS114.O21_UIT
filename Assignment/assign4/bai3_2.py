import sys
from collections import deque
def main():
    ip=list(map(int,sys.stdin.readline().split()))
    arr=deque([])
    while(len(ip)>1):
        if(len(ip)==2):
            if(ip[0]==0):
                arr.appendleft(ip[1])
            if(ip[0]==1):
                arr.append(ip[1])
        else:
            try:
                index = arr.index(ip[1])
                arr.insert(index+1,ip[2])
            except ValueError:
                arr.insert(0,ip[2])
        ip=list(map(int,sys.stdin.readline().split()))
    print(*arr)
if __name__ == '__main__':
    main()