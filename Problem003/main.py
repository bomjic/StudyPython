import time
#from ams import load_db

def calc_primefactor(primefactor):
    primefactors = []

    while primefactor != 1:
        divisor = 2
        while divisor < primefactor + 1:
            if primefactor % divisor == 0:
                primefactors.append(divisor)
                print(divisor)
                primefactor /= divisor
                break
            divisor += 1
    return primefactors

if __name__ == "__main__":
    #calc_primefactor(28)
    calc_primefactor(600851475143)