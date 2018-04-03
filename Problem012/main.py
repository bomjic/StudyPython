import sys



if __name__ == "__main__":
    sys.path.append("/home/mikhail/Documents/StudyPython/Problem003")
    from Largest_prime_factor import calc_primefactor
    triang_num_counter = 1
    factors_amount = 0

    #while triang_num_counter < 10:
    while factors_amount < 500:
        counter = 1
        triang_num = 0

        # finding triangular numbers
        for counter in range(1, triang_num_counter+1):
            triang_num += counter
            counter += 1

        #for factor in range(1, triang_num//2+1):
        #    if (triang_num % factor == 0):
        #        factors.append(factor)


        prime_factors = []
        prime_factors = calc_primefactor(triang_num)
        unique_prime_factors = set(prime_factors)

        factors_amount = 1
        for factor in unique_prime_factors:
            factors_amount *= prime_factors.count(factor)+1

        #print triang_num
        #print factors_amount
        triang_num_counter += 1

    print triang_num
    print factors_amount