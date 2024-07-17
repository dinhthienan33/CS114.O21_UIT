from itertools import product
def solve(grid,h,w,k,totalcells,black_cells_per_row,black_cells_per_column):
    count=0
    for rowchoice in product([True, False], repeat=h):
        for colchoice in product([True, False], repeat=w):
            blackcells = totalcells
            for i in range (h):
                if rowchoice[i]:
                    blackcells -= black_cells_per_row[i]
            for j in range (w):
                if colchoice[j]:
                    blackcells -= black_cells_per_column[j]
            for i in range(h):
                for j in range (w):
                    if rowchoice[i] and colchoice[j] and grid[i][j] == '#':
                        blackcells += 1
            if blackcells == k:
                count += 1
    return count
def main():
    h,w,k = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    black_cells_per_row = [row.count('#') for row in grid]
    black_cells_per_column = [col.count('#') for col in zip(*grid)]
    total = sum(black_cells_per_row)
    result=solve(grid,h,w,k,total,black_cells_per_row,black_cells_per_column)
    print(result)

if __name__ == "__main__":
    main()