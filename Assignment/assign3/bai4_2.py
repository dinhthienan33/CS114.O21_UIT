import sys
def solve(n, arr, k, x):
    l, r = 0, n - k
    while l < r:
        mid = (l + r) // 2
        if x - arr[mid] > arr[mid + k] - x:
            l = mid + 1
        else:
            r = mid
    return arr[l:l+k]
def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    k,x = map(int, sys.stdin.readline().split())
    result=solve(n,arr,k,x)
    for x in result:
       sys.stdout.write(str(x)+' ')
if __name__ == '__main__':
    main()