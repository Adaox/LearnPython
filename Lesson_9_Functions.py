# calculator take an input of your weight in kgs or lbs
# return your weight in pounds or kgs


def weight_conversion_ptk(weight):
    kgs = weight/2.2
    return kgs


def weight_conversion_ktp(weight):
    lbs = weight*2.2
    return lbs


# Fahrenheit --> Celsius and Celsius --> Fahrenheit
def temp_conversioin_ftc(temp):
    c = (temp - 32) * 5/9
    return c


def temp_conversion_ctf(temp):
    f = (temp * 9/5) + 32
    return f


print('Unit converter\n')
# weight conversion selection kgs or pounds
print('Select 1: Pounds to Kilograms')
print('Select 2: Kilograms to Pounds')
# temp conversion selection F or C
print('Select 3: Fahrenheit to Celsius')
print('Select 4: Celsius to Fahrenheit\n')
while True:
    try:
        selection = int(input('Make Your Selection: '))
        if selection in range(1, 5):
            break
    except ValueError:
        print('Please Select 1, 2, 3, or 4')
# user enters weight or temp
user_input = float(input('Enter Number To Convert: '))

if selection == 1:
    print('Your Weight in Kilograms is: ', weight_conversion_ptk(user_input))
elif selection == 2:
    print('Your Weight in Pounds is: ', weight_conversion_ktp(user_input))
elif selection == 3:
    print(f'{user_input} degrees Fahrenheit is : ',
          temp_conversioin_ftc(user_input), 'degrees Celsius')
elif selection == 4:
    print(f'{user_input} degrees Celsius is : ',
          temp_conversion_ctf(user_input), 'degrees Fahrenheit')
