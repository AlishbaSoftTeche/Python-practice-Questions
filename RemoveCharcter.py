'''Write a program to remove characters from a string starting from zero
up to n and return a new string.'''

# OUTPUT  remove_chars("pynative", 2)
# OUTPUT  remove_chars("pynative", 4)


def remove_char(word, n):
    print("orignal word ",word)
    x = word[n: ]
    return x
print(remove_char("pynative", 2))
print(remove_char("pynative", 4))