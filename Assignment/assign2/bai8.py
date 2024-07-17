import sys

def solve(arr,n):
    count_false = 0
    arr_1=arr[:n//2]
    if(n/2 ==0):
        arr_2=arr[n//2+1:]
    else : arr_2=arr[n//2:]
    arr_2=arr_2[::-1]
    for i in range(len(arr_1)):
        if(arr_1[i]!=arr_2[i]):
            count_false +=1
            if(count_false>1):
                return "FALSE"
    return "TRUE"
def is_palindrome(s):
    return s == s[::-1]
def main():
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        arr.append(x)
    print(solve(arr,n))
if __name__ == "__main__":
    main()