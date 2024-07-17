def search_unordered_array(arr, target):
    hash_table = {}
    n=len(arr)-1
    # Create a hash table with elements as keys and indices as values
    for i, num in enumerate(range(n, -1, -1)):
        hash_table[num] = i

    # Search for the target in the hash table
    if target in hash_table:
        return hash_table[target]
    else:
        return -1
arr=[3,2,5,6,7,8,9,10]
print(search_unordered_array(arr,3))