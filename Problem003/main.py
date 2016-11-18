import time

primefactor = 600851475143
primefactors = []

while primefactor != 1:
    divisor = 2
    while divisor < primefactor + 1:
        if primefactor % divisor == 0:
            print(divisor)
            primefactor /= divisor
            break
        divisor += 1
