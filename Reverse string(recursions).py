### Function reverse
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

### Driver code
s = str(input("Enter the string to reverse: "))

print('The reversed String is: ',end='')
print(reverse(s))