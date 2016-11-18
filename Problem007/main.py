import time

prime = [2]
number = 3

while len(prime) < 10001:
    for divisor in prime:
        if number % divisor == 0:
            break
        if divisor == prime[-1]:
            prime.append(number)
    number += 1

    print(prime[-1])
