def calculate_BMI(height, weight):
    BMI = weight/height**2
    return BMI

family : list[str] = ['Huy', 'Thu', 'Thanh', 'Thu-Khanh', 'Hong-Duc']
heights : dict[str, float] = dict()
weights : dict[str, float] = dict()
BMIs : dict[str, float] = dict()

for person in family:
    print (f'Hello {person}!')
    heights[person] = float(input('How tall are you?'))
    weights[person] = float(input('How much do you weigh?'))
    BMIs[person] = calculate_BMI(heights[person], weights[person])

    
print(f'Our BMIs are... {BMIs}')


