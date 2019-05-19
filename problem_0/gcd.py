# using Euclidean Algorithm

# obivious way
def gcd(x, y):
    if x == 0:
        return y
    
    if y == 0:
        return x
    
    if x < y:
        (x, y) = (y, x)
    
    return gcd(x%y, y)

# another way
def gcd_1(a, b):
    if a < b:
        return gcd_1(b, a)
    
    while b != 0:
        (a, b) = (b, a%b)
    
    return a

if __name__ == "__main__":
    assert gcd(4, 6) == 2
    assert gcd(0, 6) == 6
    assert gcd_1(234, 546) == 78
    assert gcd_1(234, 0) == 234

    print('---> all passed')