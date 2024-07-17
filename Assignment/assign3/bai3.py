import sys
import time
def main():
    ctime=time.time()
    count=0
    m,n = map(int,sys.stdin.readline().split())
    arr_m = list(map(int, sys.stdin.readline().split()))
    arr_n = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        x=search(arr_m,arr_n[i])
        if(x!=-1):
            count+=1
    print(count)
    
def search(arr, target):

  low = 0
  high = len(arr)-1

  while low <= high:

    mid = (low + high)//2

    if arr[mid] == target:
      return mid
    
    elif arr[mid] < target:
      low = mid + 1
    
    else: 
      high = mid - 1

  return -1


if __name__ == '__main__':
    main()