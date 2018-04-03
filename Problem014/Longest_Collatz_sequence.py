def calc_sequence(num):
    seq = [num]
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3* num + 1
        seq.append(num)
    return seq



if __name__ == "__main__":
    longest_seq = 0
    calculated_seq = []
    biggest_num = 0

    for num in range(1000000, 10000, -1):
        calculated_seq = calc_sequence(num)
        if len(calculated_seq) > longest_seq:
            biggest_num = num
            longest_seq = len(calculated_seq)
            print calculated_seq
            print biggest_num

    print biggest_num