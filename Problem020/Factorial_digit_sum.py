import math

def count_sum_of_digits(number):
    factorial = str(math.factorial(number))
    summ = 0
    for i in factorial:
        summ += int(i)

    return summ


if __name__ == "__main__":
    print count_sum_of_digits(10)