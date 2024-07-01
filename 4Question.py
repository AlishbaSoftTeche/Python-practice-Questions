'''Write a function to return True if the first and last number of a given
list is same.If numbers are different then return False.'''

list1 = [10,23,45,67,85,76,10]
list2 = [12,34,23,456,67,78,345]

if list1[0]==[-1]:
    print("True")
else:
    print("False")

#  This can also be done using Function

def list(numberlist):
    num1 = numberlist[0]
    num2 = numberlist[-1]

    if num1 == num2:
        return True
    else:
        return False

number_x = [10,23,34,56,67,87,98,76,10]

print("Result is",list(number_x))
number_y = [10,23,34,56,67,87,98,76,123]
print("Result is",list(number_y))