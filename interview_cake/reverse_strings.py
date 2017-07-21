
message = 'find you will pain only go you recordings security the into if'

reverse_words(message)
# returns: 'if into the security recordings you go only pain will you find'

def reverse_words(message):
    message_list = message.split()
    left_pointer = 0
    right_pointer = len(message_list)-1

    while left_pointer<right_pointer:
        message_list[left_pointer], message_list[right_pointer] = \
            message_list[right_pointer], message_list[left_pointer]

        left_pointer +=1
        right_pointer -= 1

    return " ".join(message_list)