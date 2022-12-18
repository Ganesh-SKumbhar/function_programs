# prog 4
# program to reverse given string

def rev_str(string):
    res = string[::-1]
    return res


str1 = input('Enter text : -\n')
print('Reverse of text you entered is:\n', rev_str(str1))
