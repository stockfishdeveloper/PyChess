def popcount(b):
    return bin(b).count("1")
def lsb(b):
    number = [b & -b]
    low = [-1]
    while(number[0]):
        number[0] >>= 1
        low[0] += 1
    return low[0]
