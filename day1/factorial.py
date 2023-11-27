# num = int(input('Enter a number : '))
# # print(num)
# factorial = 1
# if num < 0:
#     print('Factorial is not defined for negative numbers')
# elif num == 0:
#     print('the factorial of zero is one')
# else:
#     for i in range(1,num+1):
#         factorial = factorial*i

#     print('factorial of ',num,' is : ',factorial)

    
#  Recursion

def factorial(x):
    if x == 1:
        return 1
    else:
        return ( x * factorial(x-1))
    
num = int(input('Please enter a number :'))
result = factorial(num)
print('factorial of ',num,' is : ',result)