# prog 7
# program to find count of uppercase and lowercase characters in given string

def letter_case(s):
    lower = upper = space = special = 0
    for i in s:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isspace():
            space += 1
        else:
            special += 1
    return upper, lower, space, special


str1 = input("Enter sentence to get count of uppercase and lowercase letters count : \n")
result = letter_case(str1)
print('---------------------------------')
print(f' Upper case letters count : {result[0]} \n Lower case letters count : {result[1]}'
      f' \n Space count : {result[2]}\n Special characters : {result[3]}')
