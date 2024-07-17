import heapq as h

def remove_number(heap, number):
    for i in range(len(heap),):
        if(heap[i]==number):
            heap[i] = float('-inf')
    h.heapify(heap)    

    while heap[0] == float('-inf'):
        h.heappop(heap)  # Remove all occurrences of negative infinity
    return heap 
arr=[5, 9, 7, 1, 3,9,1,2,3,4,5,9,9,9,9]
# h.heapify(arr)
# print(arr)
k=h.nlargest(1,arr)
# print(remove_number(arr,9))
print(k[0])