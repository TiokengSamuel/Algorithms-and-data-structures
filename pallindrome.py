###Pallindrome function
def reverse(s):
    return s[::-1]


def isPallindrome(s):
    rev = reverse(s)

    if s == rev:
        return True
    else:
        return False


### Driver code

string = str(input('Enter a String to check for pallindrome: '))
ans = isPallindrome(string)

if ans == True:
    print('The String', string, 'is a pallindrome')
else:
    print('The String', string, 'is not a pallindrome')
