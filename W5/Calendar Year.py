def leap_year(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True

def day_of_week_jan1(year): # 0-Sunday, 1-Monday, ..., 6-Saturday
    r4 = (year-1) % 4
    r100 = (year-1) % 100
    r400 = (year-1) % 400
    d = (1 + 5*r4 + 4*r100 + 6*r400) % 7
    return d

def num_days_in_month(month_num,leap_year):
    if month_num in [1,3,5,7,8,10,12]:
        return 31
    elif month_num in [4,6,9,11]:
        return 30
    elif month_num==2:
        if leap_year:
            return 29
        else:
            return 28
    else:
        return None   

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    # lists can be on multiple lines if you split on the comma. Don't make a line excessively long.
    month_list = ["January", "February", "March", "April", 
                  "May", "June", "July", "August",
                  "September", "October", "November", "December"
                 ]
    result = []
    result.append(month_list[month_num-1])
    
    # There are multiple ways to do this.
    # Another possibility is if you notice that each line/week has 7 elements
    # Make a long list of all the days and then extract 7 elements each time for the weeks.
    
    week = []                      # put days in here, then join them. (more efficient)
    counter = first_day_of_month   # counts days of the week
    
    for i in range(counter):
        week.append("   ")         # 3x spaces for each day
    
    for i in range(1, num_days_in_month+1):
        week.append("%3d" % i)     # add the date, 3d means width 3. 
        counter += 1
        if counter == 7:           # end of the week
            line = "".join(week)   # joined here. (See python doc str.join)
            result.append(line)
            week = []              # reset week
            counter=0              # reset day counter
    
    if week:                       # if last week still has some dates not added
        line = "".join(week)
        result.append(line)
    
    return result

def construct_cal_year(year):
    result=[year]
    first_day_of_month = day_of_week_jan1(year)
    for i in range(12):
        num_days = num_days_in_month(i+1,leap_year(year))
        month = construct_cal_month(i+1, first_day_of_month, num_days)
        result.append(month)
        
        # get first day of month for next month
        first_day_of_month += num_days
        first_day_of_month = first_day_of_month%7
    
    return result

def display_calendar(calendar_year):
    cal_year = construct_cal_year(calendar_year)
    display = []
    for month in cal_year[1:]:                   # The first element is the year itself. Skip it.
        month.insert(1, "  S  M  T  W  T  F  S") # month is a list, insert the day headers after the month name.
        display.append("\n".join(month))         # See python doc str.join
    return "\n\n".join(display)