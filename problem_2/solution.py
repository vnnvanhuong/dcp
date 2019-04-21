def newArr(arr):

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