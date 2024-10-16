user = input('Please enter - any one-digit number or a name: ')

is_num = None

try:
    user = int(user)
    is_num = True
except ValueError:
    is_num = False

if is_num and user > 7:
    print('Hello!')
elif not is_num and user == 'John':
    print('Hello John!')
elif not is_num:
    print("There's no such name.")


print('Please enter numeric array elements one by one, or any text if done: ')
alist = []

while True:
    x = input()
    try:
        float(x)
    except:
        print('only numeric items are accepted')
        break
    alist.append(x)


print('Output array: ')


for item in alist:
    if float(item) % 3 == 0:
        print(item)
    
