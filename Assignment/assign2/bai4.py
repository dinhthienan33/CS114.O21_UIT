def main():
    m,n=map(int,input().split())
    grid=[]
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    total=0
    for row in grid:
        total+=sum(num for num in row)
    total*=4
    count=0
    for row in grid:
        for i in range(n-1):
            if(row[i]==1 and row[i+1]==1):
                count+=1
    for col in zip(*grid):
       for i in range(n-1):
            if(col[i]==1 and col[i+1]==1):
                count+=1 
    result=total-count*2
    print(count)
if __name__ == '__main__':
    main()