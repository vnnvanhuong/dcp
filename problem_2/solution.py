def newArr(arr):
    """
    MapReduce: O(n^2)
    1. Map: construct the Map with Key is each element and Value is the array
    2. Reduce: product all element of Value except the key
    """

    result = []
    hashmap = {}
    for i in arr:
        hashmap[i] = arr
    
    for key, value in hashmap.items():
        product = 1
        for v in value:
            if (v != key):
                product *=v
        result.append(product)
    
    return result


def optimizedNewArr(arr):
    """
    Ref: https://www.geeksforgeeks.org/a-product-array-puzzle/ O(n)
    1) Construct a temporary array left[] such that left[i] contains product of all elements on left of arr[i] excluding arr[i].
    2) Construct another temporary array right[] such that right[i] contains product of all elements on on right of arr[i] excluding arr[i].
    3) To get prod[], multiply left[] and right[].
    """
    result = []

    
    temp = 1
    for i in range(len(arr)):
        result.append(temp)
        temp *= arr[i]
    
    temp = 1
    j = len(arr) - 1
    while (j >= 0):
        result[j] *= temp
        temp *= arr[j]
        j -= 1
    
    return result