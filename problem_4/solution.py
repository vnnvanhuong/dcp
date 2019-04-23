def find(arr: list) -> int:
    
    i = 1
    while(True):
        count = 0
        for j in arr:
            if (i != j):
                count += 1
            if (count == len(arr)):
                return i
        i += 1