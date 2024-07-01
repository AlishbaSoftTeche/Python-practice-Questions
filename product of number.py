'''Given two integer numbers, return their product only if the
product is equal to
or lower than 1000. Otherwise, return their sum.'''

a1= int(input("Enter value of a1: "))
a2= int(input("Enter value of a2: "))

if(a1*a2<1000):
    print("prdct is =" ,a1*a2)

else:
    sum= a1+a2;
    print("Sum is =: ",sum)
print("program is finished ")

# Another way is by creating function

def product_or_sum_of_two(num1,num2):
    if num1*num2 <1000:
        print("prduct = ",num1*num2)
    else:
        print('sum of num1 and num2 = ',num1+num2)

product_or_sum_of_two(30,20)
product_or_sum_of_two(40,30)
