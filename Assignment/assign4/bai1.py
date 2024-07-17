from sys import stdin,stdout
import heapq as h
def main():
    arr=[]
    n,m=map(int,stdin.readline().split())
    for _ in range(n):
        x=int(input())
        h.heappush(arr,-x)
    for _ in range(m):
        x=input()
        k=arr[0]
        if(len(x)==2):    
            a=int(x)
            if(a==-1):
                h.heappop(arr)
            else:
                while(arr[0]==k):
                    h.heappop(arr)
        else:
            a,b=map(int,x.split())
            if(a==-3):
                k+=b
                h.heappushpop(arr,k)
            if(a==-4):
                l=k
                l+=b
                while(arr[0]==k):
                    h.heapreplace(arr,l)
    for _ in range (len(arr)):
        print(-h.heappop(arr))
# def sub_number(arr,number,b):
#     for i in range(len(arr)):
#         if(arr[i]==number):
#             arr[i]=+b
#     h.heapify(arr)
#     return arr
# def remove_number(heap, number):
#     for i in range(len(heap)):
#         if(heap[i]==number):
#             heap[i] = float('-inf')
#     h.heapify(heap)    
#     while heap[0] == float('-inf'):
#         h.heappop(heap)  # Remove all occurrences of negative infinity
#     return heap  
if __name__ == '__main__':
    main()