def find_list(numbers):
    low  = 0
    high = len(numbers) -1

    while low <= high:
        mid = (low + high) // 2
        if numbers[0] <= numbers[mid]:
            high = mid -1
        else:
            low = mid +1
        if low +1 == high:
            return mid



def find_rotation_point(words):

    low = 0
    high = len(words)-1

    while low<high:
        mid  = (low+high)//2
        if words[0] >= words[mid]:
            high = mid - 1
        else:
            low = mid + 1

        if low +1 == high:
            return low




  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
      'undzz',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

find_list(words)
find_rotation_point(words)