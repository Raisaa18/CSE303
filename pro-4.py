def sum_of_square_series(num):
    total = 0

    total = (num * (num + 1) * (2 * num + 1)) / 6

    for i in range(1, num + 1):
        if(i != num):
            print("%d^2 + " %i, end = ' ')
        else:
            print("{0}^2 = {1}".format(i, total))


num = int(input("Please Enter any Positive Number  : "))
sum_of_square_series(num)