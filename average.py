
numbers :list[int] = []


while True:
    answer :str = input('Please enter a number, x to finish ')

    if answer == 'x':
        break

    numbers.append(int(answer))



sum :int = 0
for x in numbers:
    print(x)
    sum =sum + x
    
mean :float = sum / len(numbers)
print(mean)