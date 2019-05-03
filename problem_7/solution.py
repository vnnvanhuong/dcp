# since the given message is always decodable, there is at least one way to decode
# next, we accumulate one more way whenever we find any number with 2 digits that lesser than 26
def count(str):
    
    if (len(str) == 1):
        return 1 # easy to see
    
    count = 1 # at least one way to decode
    current_idx = 0
    next_idx = 1
    while(next_idx < len(str)):
        pair = str[current_idx] + str[next_idx]

        if(int(pair) <= 26):
            count += 1
        current_idx += 1
        next_idx += 1
    
    return count