def power_digit_sum(base, exponent):
    result = 1
    exp_res = str(base ** exponent)
    print exp_res
    for i in exp_res:
        result += int(i)
        


    return result

if __name__ == "__main__":
    print power_digit_sum(2, 1000)