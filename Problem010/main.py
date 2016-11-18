prime = [2]
number = 3
summ = 2

while number < 2000000:
    for divisor in prime:
        if number % divisor == 0:
            break
        if divisor == prime[-1]:
            prime.append(number)
            summ += number
    number += 1

print(summ)
