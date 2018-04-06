import math

def lattice_paths_calc(length, width):
    return math.factorial(length + width)/(math.factorial(length) * math.factorial(width))


if __name__ == "__main__":
    print lattice_paths_calc(20,20)

