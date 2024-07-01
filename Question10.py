'''Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that
the new list should contain odd numbers from the first list and even numbers from the
 second list.'''


def merge_list(list1,list2):
    result_list = []

    for num in list1:
        if num %2!=0:
            result_list.append(num)

    for num in list2:
        if num % 2 ==0:
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print("merged list is",merge_list(list2,list2))