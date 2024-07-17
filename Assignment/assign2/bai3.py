import sys
import os
import time
start=time.time()
def solve():
    grid = []
    # for _ in range(r):
    #     row=[]
    #     row=input().split()
    #     grid.append(row)
    
    with open("test_cases.txt", "r") as f:
        r,c=f.readline().split()
        r=int(r)
        c=int(c)
        lines=f.readlines()
        for line in lines:
            row_numbers = [int(num) for num in line.split()]
            grid.append(row_numbers)
        f.close()
    
    cols = []
    maximum=[]
    for col in zip(*grid):
        cols.append(col)
        maximum.append(max_len(col))
    with open("output.txt", "w") as f:
        for i in range(r):
            formatted_row = []
            for j in range(c):
                num = str(grid[i][j]).rjust(maximum[j])
                formatted_row.append(num)
            f.write(' '.join(formatted_row) + '\n')
        f.close()
    # print(len(grid[0]))
    end=time.time()
    print(end-start)
def max_len(col):
    max_length = 0
    for num in col:
        if max_length < len(str(num)):
            max_length = len(str(num))
    return max_length

if __name__ == '__main__':
    solve()