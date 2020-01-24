def square_digits (num):
    int(num)
    sum = 0
    nemNumber = 0
    numberMerged = ""
    while(int(num)>0):
        newNumber = num%10
        newNumber = newNumber * newNumber
        numberMerged = numberMerged + str(newNumber)
        num = int(num/10)

    print(int(numberMerged))

num = 9119

square_digits(9119)

