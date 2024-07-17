
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
c = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
nx = int((-(y2 - y1)))
ny =int(x2 - x1)
C = (x2-nx,y2-ny)
D = (x1-nx,y1-ny)

E = (x1+nx,y1+ny)
F = (x2+nx,y2+ny)
print('({}, {}) ({}, {}) ({}, {}) ({}, {})'.format(x1, y1, E[0], E[1], F[0], F[1], x2, y2))
print('({}, {}) ({}, {}) ({}, {}) ({}, {})'.format(x1, y1, x2, y2, C[0], C[1], D[0], D[1]))

