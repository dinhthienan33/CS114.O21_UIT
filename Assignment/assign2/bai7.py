def main():
    l,m=map(int,input().split())
    car=[]
    left,right=[]
    for _ in range(m):
        c, x = input().split()
        c = int(c)
        if(x=='left'):
            left.append(x)
        if(x=='right'):
            right.append(x)
    left=sorted(left)
    right=sorted(right)
    count=0
    l*=100
    sum=0
    l,r=0
    for i in left:
        count_left=0
        if(sum<=l): 
            sum+=i
            left.remove(i)
            count+=1
        if(count!=0):
            l+=1
    for i in right:
        count_right=0
        if(sum<=l): 
            sum+=i
            right.remove(i)
            count+=1
        if(count!=0):
            r+=1
    

            
            
          
            
if __name__ == '__main__':
    main()
    