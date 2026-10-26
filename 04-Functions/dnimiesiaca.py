def month_name(month_number):
    if month_number == 1:
        result = 'January'
    elif month_number == 2:
        result = 'February'
    elif month_number == 3:
        result = 'March'
    elif month_number == 4:
        result = 'April'
    elif month_number == 5:
        result = 'May'
    elif month_number == 6:
        result = 'June'
    elif month_number == 7:
        result = 'July'
    elif month_number == 8:
        result = 'August'
    elif month_number == 9:
        result = 'September'
    elif month_number == 10:
        result = 'October'
    elif month_number == 11:
        result = 'November'
    elif month_number == 12:
        result = 'December'
    else:
        result = 'Unknown month'

    return result
print('The name of month 5 is', month_name(5))
print('The name of month 3 is', month_name(3))
print('The name of month 7 is', month_name(7))