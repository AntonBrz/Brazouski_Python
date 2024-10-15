int(user) = input('Please enter any one digit number: ')
if int(user) == 7:
  print('Hello!')
elif user == 'John':
  print('Hello John!')
else:
  print('There's no such name.")

print('Please enter 3 array elements: ')
alist = []
for i in range(3):
  x = input():
  alist.append(x)

print('Output array: ')
for item in alist:
  if int(item) %3 == 0:
    print(item)
    
    
