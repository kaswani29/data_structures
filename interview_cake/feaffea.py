def find_list(numbers, value):
    low  = 0
    high = len(numbers) -1

    while low <= high:
        mid = (low + high) // 2
        if value == numbers[mid]:
            return mid
        elif value< numbers[mid]:
            high = mid -1
        else:
            low = mid +1
    return False




numbers = [1,5,13,41,55,56,88]

find_list(numbers,5)