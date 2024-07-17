def main():
    m,n=map(int,input().split())
    grid=[]
    for _ in range(m):
        row=list(input())
        r=count(row)
        grid.append(r)
    print(solve(grid,m,n))
def count(lst):
    count = 1  
    consecutive_counts = []  
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            count += 1  
        else:
            consecutive_counts.append(count)  
            count = 1  
    consecutive_counts.append(count)
    return consecutive_counts
def solve(grid,m,n):
    count=0
    for i in range(m):
        for j in range(len(grid[i])-1,0,-1):
            if(j>len(grid[i]) and j>len(grid[i+1])):
                x=grid[i][j]
                sum_1=sum(grid[i][:j])
                y=grid[i+1][j]
                sum_2=sum(grid[i+1][:j])
                if(sum_1+x<=sum_2+y and sum_2<=sum_1):
                    count+=1
                else: break
    return count
if __name__ == '__main__':
    main()