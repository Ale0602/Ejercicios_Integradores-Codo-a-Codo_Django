def mcd(n1,n2):
    
    mcd = 1

    if n1 % n2 == 0:
        return n2
    
    for x in range(int(n2/2), 0, -1):
        if n1 % x == 0 and n2 % x == 0:
            mcd = x
            break

    return mcd

print(mcd(8, 4))
print(mcd(13, 7))
print(mcd(29, 19))
print(mcd(17, 12))
print(mcd(4, 2))