def multiple_3_5(number):

    total = 0

    while number > 0:

        if number%3 == 0 or number%5 == 0:
            total += number
        number -= 1

    return total


multiple_3_5(1000)