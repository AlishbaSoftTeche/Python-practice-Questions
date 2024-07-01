'''Exercise 2: Print the sum of the current number and the previous number'''

print("Printing current and previous number sum in a range(10)")

previous_number = 0
for i in range(0,10):
    x_sum = previous_number + i
    print ("Current Number", i ,"Previous Number" , previous_number," Sum: ", x_sum)

    previous_number= i ;