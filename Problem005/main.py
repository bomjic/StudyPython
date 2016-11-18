dividor = 2520
flag = False

while flag != True:
    for i in range(2, 21):
        if dividor % i != 0:
            break

    if i == 20:
        print (dividor)
        flag = True

#    if dividor % 1000000 == 0:
#        print(dividor)

    dividor += 2

