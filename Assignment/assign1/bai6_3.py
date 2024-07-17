def tachchuoi(string):
    odd=[]
    even=[]
    for i in range(len(string)):
        if(i%2!=0):
            even.append(string[i])
        else :
            odd.append(string[i])
    return sorted(odd),sorted(even)
def solve(a, b):
    odd_a, even_a = tachchuoi(a)
    odd_b, even_b = tachchuoi(b)
    if(odd_a == odd_b) and (even_a == even_b):
        return "YES"
    return "NO"
def main():
    t=int(input())
    for _ in range(t):
        a=input()
        b=input()
        print(solve(a,b))
if __name__ == "__main__":
    main()