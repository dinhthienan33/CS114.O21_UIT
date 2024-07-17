import sys
def main():
    ip=list(map(int,sys.stdin.readline().split()))
    arr=[]
    while(len(ip)>1):
        if(len(ip)==2):
            if(ip[0]==0):
                arr=[ip[1]]+arr
            if(ip[0]==1):
                arr.append(ip[1])
        else:
                index = arr.index(ip[1])
                if(index!=-1):
                    arr.insert(index,ip[2])
                else: arr.insert(0,ip[2])
        ip=list(map(int,sys.stdin.readline().split()))
    print(*arr)
if __name__ == '__main__':
    main()