BRACKET_SEQUENCE = '[((())()(())]]'

def check_correct(sequence):
    """Return False if the sequence has not paried and ordered elements.
    Print out unpaired elements."""

    if len(sequence) % 2 != 0:
        return False
    try:
        stack = []
        for element in sequence:
            if element == '(':
                stack.append(element)
            elif element == ')':
                stack.pop()
    except:
        return False


    if len(stack):
         print('Unpaired element: ', stack)
         return False

    return True



print('Given sequence: ', BRACKET_SEQUENCE)
print('Checking...')
result = check_correct(BRACKET_SEQUENCE)


if result:
    print('correct')
else:
    print('incorrect')


while True:
    user = input('Please enter your sequence, or type exit: ')
    if user == 'exit':
        break
    else:
        result = check_correct(user)
    if result:
        print('correct')
    else:
        print('incorrect')
