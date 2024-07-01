'''Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space
separating the digits.'''

number = int(input("Enter number "))
print("Number is: ",number)

while number >0:
    digit = number % 10
    number = number//10
    print(digit,end=" ")