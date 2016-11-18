summ = 0
sq_summ = 0

for i in range(1, 101):
    summ += i
    sq_summ += i ** 2

summ_sq = summ ** 2

print('summ of squares = ', summ_sq)
print('square of summs = ', sq_summ)
print('difference is ', summ_sq - sq_summ)