def main():
    l,m=map(int,input().split())
    l=l*100
    arr_left=[]
    arr_right=[]
    for _ in range(m):
        x,y=input().split()
        if(y=='left'):
            arr_left.append(int(x))
        else : arr_right.append(int(x))
    count_left=solve(arr_left,l)
    count_right=solve(arr_right,l)
    result=max(2*count_left-1,2*count_right)
    print(result)
def solve(arr,l):
    count=1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)-1):
            if(sum(arr[i:j+1])<=l):
                count+=1
                i=j+1
    return count
        
if __name__ == '__main__':
    main()