import math

for a in range(3, 1001):
    for b in range(a + 1, 1001):
        sq_c = ( a ** 2 ) + ( b ** 2 )
        c = math.sqrt(sq_c)
        if c < b:
            break
        if a + b + c == 1000:
            print (a * b * c)

