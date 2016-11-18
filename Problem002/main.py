
fibonacci = [1, 2]
evensumm = 2
summ=fibonacci[-1]
#print fibonacci[-1]

while fibonacci[-1] + fibonacci[-2] < 4000000:
    summ = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(summ)
    if summ % 2 == 0:
        evensumm += summ


print (evensumm)
print (fibonacci)
