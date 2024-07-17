def main():
    l,m = map(int,input().split())
    arr_left = []
    arr_right = []
    for _ in range(m):
        x, y = input().split()
        if y == "left":
            arr_left.append(int(x))
        else:
            arr_right.append(int(x))
    l=l*100
    count_left=solve(arr_left, l)
    count_right=solve(arr_right, l)
    result=max(2*count_left-1, 2*count_right)
    print(result)
def solve(arr,l):
    index=0
    count=0
    while (index <= len(arr)-1):
        total = 0
        while ((index <= len(arr)-1)):
            temp_sum = total + arr[index]
            if temp_sum <= l:
                total = temp_sum
                index += 1
            else:
                break
        if total > 0:
            count += 1
    return count
if __name__ == '__main__':
    main()