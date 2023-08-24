def mcm(n1, n2):
    
    y = max (n1, n2)

    while True:
        if (y % n1 == 0) and (y % n2 == 0):
            return y
        y += 1
        
print(mcm(2, 4))
print(mcm(32, 13))
print(mcm(17, 15))