

def get_string(number):
    figures = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    # amount of figures in number
    capacity = len(str(number))

    # ordered list of figures in number
    list_num = list(str(number))
    for i in range(0, len(list_num) ):
        list_num[i] = int(list_num[i])

    # ordered list divided on thousands
    list_hundreds = []
    for hundred_end in range(len(list_num), 0, -3):
        hundred_start = hundred_end - 3
        if hundred_start < 0: hundred_start = 0
        list_to_insert = list_num[hundred_start:hundred_end]
        while len(list_to_insert) != 3:
            list_to_insert.insert(0, 0)
        list_hundreds.insert(0, list_to_insert)

    thousand = len(list_hundreds)-1
    string = ""
    for triplet in list_hundreds:
        # if it's teens, then choose from them, if not, then add tens and figures
        if triplet[1] == 1:
            hundreds_string = teens[triplet[2]]
        else:
            hundreds_string = tens[triplet[1]] + figures[triplet[2]]

        # then add one hundred, two hundred e.t.c
        if triplet[0] != 0:
            if hundreds_string == "":
                hundreds_string = figures[triplet[0]] + "hundred"
            else:
                hundreds_string = figures[triplet[0]] + "hundredand" + hundreds_string
        #print triplet
        # if it's thousand billion or trillion then add it
        hundreds_string += thousands[thousand]
        #print hundreds_string
        thousand -= 1
        string += hundreds_string
    #print string
    return string




def number_letter_counts(start, end):
    string = ""
    for num in range(start, end+1):
        string += get_string(num)
    return len(string)

if __name__ == "__main__":
    print number_letter_counts(1,1000)
