def main():
    n=int(input())
    arr=[]
    for _ in range(n):
        x=int(input())
        arr.append(x)
    count_false=0
    for i in arr:
        new_arr =arr
        new_arr.remove(i)
        if(check_palindrome(new_arr)):
            print("TRUE")
            return
    for i in range(n//2):
        if (arr[i]!=arr[n-i-1]):
            count_false+=1
            if(count_false==2):
                print("FAlSE")
                return
    print("TRUE")
def check_palindrome(string):
    return string==string[::-1]
    
if __name__ == "__main__":
    main()