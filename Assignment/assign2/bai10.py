def main():
    n = int(input().strip())
    stack = list(map(float, input().strip().split()))
    x = int(input().strip())
    y = int(input().strip())
    z = float(input().strip())
    total = x * n
    count = 0
    i = 0
    while i < n:
        j = i - 1
        while j >= 0 and stack[i] - stack[j] <= z:
            total+=y
            j -= 1
        i += 1

    print(total )

if __name__ == '__main__':
    main()