# prog 13
# pangram is a string
import string
# approach 1
def str_pangram(string):
    alhpabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in alhpabets:
        if i not in string.lower():
            return False

    return True
# approach 2
def ispangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return  alphaset <= set(str1.lower())

str1 = input('Enter a string: \n')
print(str_pangram(str1))
print(ispangram(str1))