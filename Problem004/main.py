
palyndrome = 0
for multiplicand in range(100, 1000):
    for multiplier in range(100, 1000):
        result = multiplicand * multiplier
        str_result = str(result)
        #print (str_result)
        for i in range(0, len(str_result) / 2 + 1):
            if str_result[i] != str_result[-1 - i]:
                #print(str_result[i], str_result[-1 - i])
                break

            if i == len(str_result) / 2:
                if palyndrome < result:
                    palyndrome = result
print("Palyndrome ", palyndrome)