month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 1 Jan 1901
# First day of month is 1, first month is 1
date = {'day':1, 'month':1, 'year':1901}
day = 0

first_sundays = 0

while date['year'] < 2001:
    day += 1
    day_of_week = week_day[day % 7]

    if date['day'] == 1 and day_of_week == 'Sunday':
        first_sundays += 1


    if date['day'] + 1 > month_lengths[date['month'] - 1]:
        # This is sloppy
        date['month'] = (date['month'] + 1) % 13
        if date['month'] == 0:
            date['month'] = 1

        if date['month'] == 1:
            date['year'] += 1
            if date['year'] % 4 == 0 and (date['year'] % 100 != 0 or date['year'] % 400 == 0):
                month_lengths[1] = 29
            else:
                month_lengths[1] = 28
        date['day'] = 1
    else:
        date['day'] += 1

print first_sundays
