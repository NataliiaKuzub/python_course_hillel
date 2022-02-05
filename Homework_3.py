"""
This is code, which inverts the three-digit number in two different ways
"""
# First way
number = input("Please, type a number you want to reverse: ")
number = int(number)
first_num = number // 100
second_num = number % 100 // 10 * 10
third_num = number % 10 * 100
reversed_number = first_num + second_num + third_num
if (number % 100) == 0:
    print('The reversed number is: 00%s' % reversed_number)
elif (number % 10) == 0:
    print('The reversed number is: 0%s' % reversed_number)
else:
    print('The reversed number is: ', reversed_number)

# Second way
number = input("Please, type a number you want: ")
print('The reversed number is: ' + number[::-1])
