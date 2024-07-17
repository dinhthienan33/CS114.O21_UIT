import sys

def find_closest_elements(arr, k, x):
    left = 0
    right = len(arr) - k
    
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    
    return arr[left:left + k]

n = int(sys.stdin.readline())
a = ((list(map(int, sys.stdin.readline().strip().split()))))
k, x = map(int, sys.stdin.readline().strip().split())

result = find_closest_elements(a, k, x)

for num in result:
    print(num, end=" ")