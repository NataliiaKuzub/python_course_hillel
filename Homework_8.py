"""
This is a function for defining a month and a season by a number. Only numerical arguments from 1 to 12 ca be used.
"""
def months(month_num):
    seasons = {
        'winter': ('December', 'January', 'February'),
        'spring': ('March', 'April', 'May'),
        'summer': ('June', 'July', 'August'),
        'autumn': ('September', 'October', 'November')
    }
    numeration = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    if month_num not in numeration:
        return print('There are only 12 month in a year. Please, enter a number from 1 to 12.')
    else:
        for i in seasons:
            if numeration[month_num] in seasons[i]:
                season = i
        return print('Your month is', numeration[month_num]+ ', it is', season+'.')

print(months(4))
