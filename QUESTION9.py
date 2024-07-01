'''Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse.
For example, 545, is the palindrome numbers'''

def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


palindrome(121)
palindrome(125)


# Another way to do this is


def palindrome_number(word):
    left = 0
    right =len(word)-1

    while left < right:
        if word[left] != word[right]:
            return False
        left+=1
        right-=1
    return  True

word = input("Enter word: ")

if palindrome_number(word):
    print("Number is pallindrome ")
else:
    print("number is not palindrome")