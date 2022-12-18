# prog 14
# wap to accept hype separated sequence of words, and print the words in sequence sorted alphabetically

def sort_words(str1):
    str_list = str1.split('-')
    str_list.sort()
    return '-'.join(str_list)


user_str = input('Enter hype separated list of words: \n')
print('sorted list : \n', sort_words(user_str))
