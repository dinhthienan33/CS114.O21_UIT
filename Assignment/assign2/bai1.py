def extract_edges(grid, i):
    m, n = len(grid), len(grid[0])
    edges = []
    if(i==n-1-i and i==m-i-1): 
        edges.append(grid[i][n-i])
    elif(i==n-i-1):
        for j in range(i,m-i):
            edges.append(grid[j][i])
    elif(i==m-i-1):
        for j in range(i,n-i):
            edges.append(grid[i][j])
    else:
        for j in range(i, n - i):
            edges.append(grid[i][j])
        for k in range(i + 1, m - i):
            edges.append(grid[k][n - i - 1])
        for j in range(n - i - 2, i - 1, -1):
            edges.append(grid[m - i - 1][j])
        for k in range(m - i - 2, i, -1):
            edges.append(grid[k][i])

    return edges
def clockwise(arr):
    return arr[-1:] + arr[:-1]

def un_clockwise(arr):
    return arr[1:] + arr[:1]
def solve(grid, m, n):
    mi=min(m,n)
    if(mi%2!=0):
        mi+=1
    for i in range((mi//2)):
        arr = extract_edges(grid, i)
        if i % 2 == 0:
            arr = clockwise(arr)
        else:
            arr = un_clockwise(arr)
        index = 0
        if(i==n-i-1 and i==m-i-1): 
            (grid[i][n-i])=arr[index]
        elif(i==n-i-1):
            for j in range(i,m-i):
                grid[j][i]=arr[index]
                index+=1              
        elif(i==m-i-1):
            for j in range(i,n-i):
                grid[i][j]=arr[index]
                index+=1
        else:
            for h in range(i, n - i):
                grid[i][h] = arr[index]
                index += 1
            for k in range(i + 1, m - i):
                grid[k][n - i - 1] = arr[index]
                index += 1
            for h in range(n - i - 2, i - 1, -1):
                grid[m - i - 1][h] = arr[index]
                index += 1
            for k in range(m - i - 2, i, -1):
                grid[k][i] = arr[index]
                index += 1
    return grid
def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))
def main():
    m,n=map(int,input().split())
    grid=[]
    for _ in range(m):
         row=list(map(int,input().split()))
         grid.append(row)
    result=solve(grid,m,n)
    print_grid(result)

            
    
if __name__ == '__main__':
    main()