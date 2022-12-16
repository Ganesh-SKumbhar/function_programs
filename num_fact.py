# prog 5
# find factorial of positive number

def fact(num):
    if num == 0:
        return 1
    else:
        count = 1
        res = 1
        while count <= num:
            res = count * res
            count += 1
        return res


number = int(input('Enter a number to find its factorial: \n'))
if number < 0:
    print('please enter positive number')
else:
    print(f'Factorial of {number} (i.e. {number}! ) is :-- {fact(number)}')

