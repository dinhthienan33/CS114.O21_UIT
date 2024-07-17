def main():
    t=int(input())
    for _ in range(t):
        a=input().lower()
        b=input().lower()
        print(solve(a,b))
def solve (a,b):
    if(len(b)%2==0) or (len(a)!=len(b)):
        return "NO"
    for i in range(len(b)):
        if(a.find(b[i])==-1):
            return "NO"
    if len(set(a))==len(set(b)):
        return "YES"
    return "NO"
if __name__ == "__main__":
    main()