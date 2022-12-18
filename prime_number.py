# prog 9
# find whether number is prime

def is_prime(num):
    if num == 1:
        return 'not a prime number'
    elif num == 2:
        return 'is prime number'
    else:
        for i in range(2, num):
            if num % i == 0:
                return 'not a prime number'
        return 'prime number'


numb = int(input('Enter any number : \n'))
print(is_prime(numb))
