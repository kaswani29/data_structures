

def sum_even_fibonacci(number):
    if number in [0, 1]:
        return number

    prev_prev = 0
    prev = 1
    total = 0
    fib_num = 0

    while fib_num <= number:

        fib_num = prev_prev + prev

        if fib_num % 2 == 0:
            total += fib_num

    return total


sum_even_fibonacci(4000000)