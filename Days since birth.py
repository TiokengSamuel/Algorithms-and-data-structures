###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###
year = int(input("Enter the year:  "))
month = int(input("Enter the month: "))
day  = int(input("Enter the day: "))


def nextDay(year, month, day):
    pass
    # Your Code
    if day < 30:
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1

ans = nextDay(year, month, day)

print (ans)




