print (" hello Hong-Duc")
a = 3
b = 4
print (a*b)
print('enter your name')
name = input()
print('hello, ' + name)
print(f'hello {name} again')
if name.lower() == 'hong-duc':
	print (f'{name}, you are the youngest child')
elif name.lower() == 'huy':
	print(f'you are the oldest')
else:
	print(f'I do not know you, {name}')

print ('enter a command')
command = input()

while command.lower() != 'finish':
	print(f'Error, {command} is not valid')
	print('please try another command')
	command = input()

for set in range(1,4):
	for rep in range(1,11):
		print(f'you are on {rep}, {10 -rep} more to go!')
	print(f'You completed set {set}!') 


name : list[str] = ['Huy', 'Thu', 'Thanh', 'Thu-Khanh', 'Hong-Duc']
empty_list = []

#append adds item to list
print(empty_list)
empty_list.append('fish')
empty_list.append('cat')
empty_list.append('fish')
empty_list.append('dog')
empty_list.append('rabbit')
empty_list.append('fish')

#len counts how many items are in list
print(len(name))
print(empty_list.count('fish'))
 


#extend combinds lists or adds items to list
belongings = ['torch','tent','matches','clothes']
pets = ['fish','dog','cat']

print(belongings)
print(pets)

belongings.extend(pets)

print(belongings)

#prints individual ietms in list
print(belongings[1])
print(belongings[3])

#index shows where item is in list
print(belongings.index('dog'))



#insert inserts item or list at certain index
vehicles = ['ferrari', 'mclaren', 'koenigsegg', 'lamboghini']
motorbikes = ['yamaha', 'mizubishi', 'honda']

vehicles.insert(3, motorbikes)

#pop removes item from list
print(vehicles)
removed_vehicle = vehicles.pop(3)
print('pop(3):', removed_vehicle)
print(vehicles)


#remove removes first occurence of item in list
fruit = ['apple', 'pear','bananna','apple','pear','pineapple']
print(fruit)
fruit.remove('pear')
print(fruit)

#reverse reverses order of list
fruit.reverse()
print(fruit)

#sort sorts list in assigned order
fruit.append('orange')
fruit.append('pear')
fruit.append('pear')

fruit.sort()
print(fruit)

def sort_by_length(input_string):
	return len(input_string)

fruit.sort(key = sort_by_length)
print('After sort(key = sort_by_length', fruit)

numbers = [1,3,3,7,9]
print(numbers)
print(numbers[4])

print('this number is...', numbers[0])
print('this number is...', numbers[1])
print('this number is...', numbers[2])
print('this number is...', numbers[3])
print('this number is...', numbers[4])


for i in range (0,5):
    print('this number is...', numbers[i])

print()

items = len(numbers)
for i in range (0,items):
    print(i)
    print('this number is...', numbers[i])

print()

for x in numbers:
    print('this number is...', x)
    
print()

for x in numbers:
    if x > 3:
    	print('this number is...', x)
        
print()

[print('this number is greater than 3...', x) for x in numbers if x > 3]

print()

items = len(numbers)
for x in range (0,items):
    print('the number at position', x, 'is', numbers[x])
    
print()
    
for i,x in enumerate(numbers):
    print('The number at position ',i, 'is',x)