import bisect
from sys import stdin,stdout
def main():
    n=input()
    arr=list(map(int,stdin.readline().split()))
    while(1):
        b=list(map(int,stdin.readline().split()))
        if len(b)==0:
            break
        else:
            result=solve(b[0],b[1],arr)
            m,n=min(result),max(result)
            print(m,n)
def find_index(lst,x):
    i=bisect.bisect_left(lst,x)
    return i

def solve(k,x,lst):
    lst_result=[]
    pos=find_index(lst,x)

    if pos==0:
        return lst[0:k]
    elif pos>=len(lst)-1:
        return lst[len(lst)-k:len(lst)]
    else:
        l=pos
        r=pos+1
        if lst[pos]==x or x-lst[l] <= lst[r]-x:
            lst_result.append(lst[pos])
            l-=1
        else:
            lst_result.append(lst[pos+1])
            r+=1
        count=1

        while(count!=k):
            if l<0 and r<len(lst)-1 : 
                lst_result.append(lst[r])
                r+=1
            elif r>len(lst)-1 and l>=0: 
                lst_result.append(lst[l])
                l-=1
            else:
                if x-lst[l] <= lst[r]-x:
                    lst_result.append(lst[l])
                    l-=1
                else:
                    lst_result.append(lst[r])
                    r+=1
            count+=1
    return lst_result


if __name__ == "__main__":
    main()