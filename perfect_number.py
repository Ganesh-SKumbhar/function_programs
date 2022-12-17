# prog 11
# check whether number is perfect or not


def perfect_num(num):
    temp = []
    for i in range(1, num + 1):
        if num % i == 0:
            temp.append(i)
    if (sum(temp[:-1]) == num) and (sum(temp)//2 == num):
        return '-->> is a Perfect number'
    else:
        return 'is not perfect'


n = int(input('Enter number to check whether it is perfect or not: \n'))
print(n, perfect_num(n))
