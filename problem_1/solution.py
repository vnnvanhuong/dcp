def check(arr, k):
    if (len(arr) == 0):
        return False
    
    if (len(arr) == 1):
        return arr[0] == k
        
    if (len(arr) == 2):
        return arr[0] + arr[1] == k

    for i in arr:
        rest = k - i
        index_i = arr.index(i)+1
        new_arr = arr[index_i:]
        for j in new_arr:
            if (j == rest):
                return True
    
    return False