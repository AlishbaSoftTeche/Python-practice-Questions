'''Iterate the given list of numbers and print only those
numbers which are divisible by 5'''

num_list = [12,34,56,678,5,70,45,32]
print("given list is ",num_list)
print("divisible by 5 ")
for num in num_list:
    if num % 5 == 0:
        print(num)
