bracket_sequence = '[((())()(())]]'

def check_correct(sequence):
    if len(sequence) % 2 != 0: return False

    stack = []
    try:
        for element in sequence:
            if element == '(':
                stack.append(element)
            elif element == ')':
                stack.pop()
        print(stack)
        if len(stack): return False
    except:
        return False

    return True



result = check_correct(bracket_sequence)

if result:
    print('correct')
else:
    print('incorrect')


result = check_correct('[((()]')

if result:
    print('correct')
else:
    print('incorrect')
