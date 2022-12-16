# prog 3
# multiplication of numbers in list

def mult_list(num_list):
    res = 1
    for i in num_list:
        res *= int(i)
    return res


lst = input('Enter the list of numbers separated by ",": - ').split(',')
print('Multiplication of list elements is: ', mult_list(lst))
