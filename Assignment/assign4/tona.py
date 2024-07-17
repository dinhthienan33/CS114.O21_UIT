def draw(n):
    if(n<1): return 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            print('*')
    draw(n-3)
draw(3)