def main():
    r,c=map(int,input().split())
    grid=[]
    for _ in range(r):
        row=[]
        row=input()
        grid.append(row)
    n=len(grid)
    for i in range(n//2):
        grid[i], grid[n-i-1] = grid[n-i-1], grid[i]
    for row in grid:
        print(row)
if __name__ == "__main__":
    main()