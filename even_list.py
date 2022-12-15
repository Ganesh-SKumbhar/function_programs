# prog 10
# wap to print even numbers from given list
"""
def find_even(lst):
    for i in lst:
        if int(i) % 2 == 0:
            print(i,  end='  ')


num_list = input('enter a list of numbers separated by "," : \n').split(',')
find_even(num_list)
"""


def find_even(lst):
    even = []
    for i in lst:
        if int(i) % 2 == 0:
            even.append(i)
    return even


num_list = input('enter a list of numbers separated by "," : \n').split(',')
print('List of even numbers is :-- ', find_even(num_list))
