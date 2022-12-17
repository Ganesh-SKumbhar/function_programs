# prog 12

def palindrome(str1):
    str2 = str1[::-1]
    if str2 == str1:
        return 'string is palindrome'
    else:
        return 'not palindrome'


u_str = input('Enter string to check whether it is palindrome: \n')
print(palindrome(u_str))
