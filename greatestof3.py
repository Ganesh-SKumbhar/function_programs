# prog 1
'''
def greatest_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


x, y, z = input('Enter 3 numbers separated by "," :').split(',')
result = greatest_num(int(x), int(y), int(z))
print(result, ' is greatest number')

'''


# one more approach
def maxi(*var):
    res = sorted(var)
    return res[-1]


x, y, z = input('Enter 3 numbers separated by "," :').split(',')
result = maxi(int(x), int(y), int(z))

print('greatest number is : ',result)

