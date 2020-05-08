
num = int(input("Enter nmber for factorial: "))

### Factorial number!!!
def factorial(num):

    return 1 if(num == 1 or num == 0) else num * factorial(num - 1)

### Driver code

print ('The factorial of', num ,'is:', factorial(num))

