""" Checking if the given year is leap year  """
def is_leap(year):
    # If it is not divisible by 4, it is not a leap year.
    # If a year is divisible by 4, but not by 100, then it is a leap year
    # If a year is divisible by 100, but not by 400, then it is not a leap year.
    # If a year is divisible by both(100 and 400), then it is a leap year
    if ((year % 400 == 0) or (year % 100 != 0)) and (year % 4 == 0):
        return True
    # else it is not a leap year
    return False


""" Find number of days in the month """
def days_in_month(year, month):
    if month not in range(1, 13):
        raise ValueError('Month Number must be between 1 and 12')
    else:
        # January, March, May, July, August, October, December have 31 days
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        if month == 2:
            # check year is leap
            # February has 29 days in a leap year
            if is_leap(year):
                return 29
            # February has 28 days
            return 28
        # April, June, September, November have 30 days
        return 30


# input year
y = int(input('Enter a year: '))
# input month
m = int(input('Enter a month: '))

# printing result
print(f'Number of days in the month: {days_in_month(y, m)}')