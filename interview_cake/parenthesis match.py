message = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

def parenthesis_match(message, value):

    stack_parentheis = []
    counter = value
    for x in message[value:]:

        if x == "(":
            stack_parentheis.append(x)
        elif x == ")":
            stack_parentheis.pop()
        if len(stack_parentheis) == 0:
            return counter
        counter +=1
        return "not found"


