import sys

def main():
    n = int(sys.stdin.readline().strip())
    points = []
    for _ in range(n):
        x, y = sys.stdin.readline().strip().split()
        x = check(x)
        y = check(y)
        points.append([x, y])

    count = 0
    for i in range(n - 2):
        if findDirct(points[i], points[i + 1], points[i + 2]):
            count += 1
    sys.stdout.write(str(count) + '\n')

def findDirct(p0, p1, p2):
    v1_x = int(p1[0]) - int(p0[0])
    v1_y = int(p1[1]) - int(p0[1])
    v2_x = int(p2[0]) - int(p0[0])
    v2_y = int(p2[1]) - int(p0[1])
    if v1_x * v2_y - v1_y * v2_x < 0:
        return True
    else:
        return False

def check(s):
    if s[0] == '‐':
        s = -int(s[1:])
    return int(s)

if __name__ == '__main__':
    main()