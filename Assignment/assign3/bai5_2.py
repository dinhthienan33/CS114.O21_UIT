import sys
def solve(n, arr, k, x):
    if x >= arr[n-1]:
        sys.stdout.write(str(arr[n-k]) + ' ' + str(arr[n-1]) + '\n')
        return
    if x <= arr[0]:
        sys.stdout.write(str(arr[0]) + ' ' + str(arr[ k - 1]) + '\n')
        return
    l, r = 0, n - k
    while l < r:
        mid = (l + r) // 2
        if x - arr[mid] > arr[mid + k] - x:
            l = mid + 1
        else:
            r = mid
    sys.stdout.write(str(arr[l]) + ' ' + str(arr[l + k - 1]) + '\n')
def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    while True:
        ip = list(map(int, sys.stdin.readline().strip().split()))
        if len(ip) == 0:
            break
        else:
            solve(n, arr, ip[0], ip[1])
if __name__ == '__main__':
    main()