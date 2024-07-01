''' Write a program to accept a string from the user and display
characters that are present at an even index number
'''

word = input("Enter word ")
print("orignal string is ",word)

x = list(word)
for i in x[0::2]:
    print(i)

# Another way to write this program is

word = input("Enter word ")
print("changed word is ", word)

size = len(word)
for i in range(0 , size - 1, 2):
    print("index [",i,"]",word[i])