### Reverse function
def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str

### Driver code
s = str(input("Enter a string to reverse(By loop method): "))

print('The reverse is:', reverse(s))
