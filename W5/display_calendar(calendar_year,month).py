def display_calendar(calendar_year,month):
    cal_year = construct_cal_year(calendar_year)
    display = []
    if month is None:
        for month_list in cal_year[1:]:
            month_list.insert(1, "  S  M  T  W  T  F  S")
            display.append("\n".join(month_list))
    else:
        month_list = cal_year[month]
        month_list.insert(1, "  S  M  T  W  T  F  S")
        display.append("\n".join(month_list))
    return "\n\n".join(display)


def display_calendar(calendar_year,month):
    cal_year = construct_cal_year(calendar_year)
    display = []
    
    # enumerate() is a Python Built-in function, see python docs.
    # Basically, it replicates
    # for i in range(len(cal_year[1:])):
    #     month_list = cal_year[1:][i]
    # Except that it produces a tuple (i, month_list) directly
    # the "for i, month_list in" does something called tuple unpacking.
    # It assigns the values in the tuple from enumerate() to the variables in order.
    
    for i, month_list in enumerate(cal_year[1:],1):
        if month is None or month==i:
            month_list.insert(1, "  S  M  T  W  T  F  S")
            display.append("\n".join(month_list))
    return "\n\n".join(display)

    '''enumerate(sequence, start=0)
The next() method of the iterator returned by enumerate() returns a 
tuple containing a count (from start which defaults to 0) and the 
values obtained from iterating over sequence
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]'''