"""
names : list[str] = ['Huy', 'Thu', 'Thanh', 'Thu-Khanh', 'Hong-Duc', "Cat"]

guess : str = input('who are you thinking of?')
"""
""""
# method 1
if guess == names[0] or guess == names[1] or guess == names[2] or guess == names[3] or guess == names[4]:
    print('you guessed right')
else:
    print(f'no, {guess} is not in my family')
"""
"""
#method 2
for i in range (0,4):
    if guess == names[i]:
        print('you guessed right')
    else:
        print(f'no, {guess} is not in my family')
"""
"""
#method 3
successful = False
for i in range (0,4):
    if guess == names[i]:
        successful = True
"""

"""
#method 4
successful = False
for i in range (0,len(names)):
    if guess == names[i]:
        successful = True

if successful == True:
    print('you guessed right')
else:
    print(f'no, {guess} is not in my family')
"""

"""
#method 4
successful = False
for x in names:
    if guess == x:
        successful = True

if successful == True:
    print('you guessed right')
else:
    print(f'no, {guess} is not in my family')


successful: bool = False
for x  in names:
    if guess == x:
        successful = True

if successful == True:
    print('you guessed right')
else:
    print(f'no, {guess} is not in my family')

"""
"""
#method 5
if guess in names:
    print('you guessed right')
else:
    print(f'no, {guess} is not in my family')

"""

binary :str = input('Enter binary ')
total = 0

readable = reversed(binary)

"""
x = 0
for b in readable:
    print(x, b, int(2^(x)))
    bit = int(b)
    total = total + bit * int(2**(x))
    x = x + 1
    """

for x, b in enumerate(readable):
    print(x, b, int(2**(x)))
    bit = int(b)
    total += bit * int(2**(x))

print(f'{binary} is equalt to, {total}')
