height = float(input('Enter your height in m:'))
weight = float(input('Enter your weight in kkg:'))

BMI = round(weight/height**2, 2)

if BMI < 18.5:
    print(f'You are underweight with {BMI}')
elif BMI < 25:
    print(f'you are normal with {BMI}')
elif BMI < 30:
    print(f'you are overweight with {BMI}')
elif BMI < 35:
    print(f'you are obese with {BMI}')

else:
    print(f'you are clinically obese with {BMI}')
