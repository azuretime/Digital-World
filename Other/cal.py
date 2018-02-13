def leap_year(year):
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0
    if (divisible_by_4 and not divisible_by_100):
        return True
    if (divisible_by_100 and divisible_by_400):
        return True
    else:
        return False
    
def day_of_week_jan1(year):
    a=(year-1)%4
    b=(year-1)%100
    c=(year-1)%400
    d = (1 + 5*a + 4*b + 6*c)%7
    return d



def num_days_in_month(month_num,leap_year):
    if month_num>0 and month_num<13:
        if leap_year == True:
            if month_num==1 or month_num==3 or month_num==5 or month_num==7 or month_num==8 or month_num==10 or month_num==12:
                return 31
            elif month_num==2:
                return 29
            else:
                return 30
        else:
            if month_num==1 or month_num==3 or month_num==5 or month_num==7 or month_num==8 or month_num==10 or month_num==12:
                return 31
            elif month_num==2:
                return 28
            else:
                return 30
                
def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    M={1:'January',2:'Feburary',3:'March',4:'April',
        5:'May',6:'June',7:'July',8:'Augest',9:'September',
        10:'October',11:'November',12:'December'}

    string=''
    for i in range(1,num_days_in_month+1):
        if i<10:
            string+='  '+str(i)
        else:
            string+=' '+str(i)
           
    string = '   '*first_day_of_month+string
     
    string= M[month_num]+'\n'+string[:21]+'\n'+string[21:42]+'\n'+string[42:63]+'\n'+string[63:84]+'\n'+string[84:105]+'\n'+string[105:]

    return string

print construct_cal_month(1, 5, 31)


    
def construct_cal_year(year):
    ls=str(year)+'\n'
    
    for i in range(12):
        first_day_of_month=day_of_week_jan1(year)
        for j in range(i):
            first_day_of_month += num_days_in_month(j+1,leap_year(year))
        first_day_of_month=first_day_of_month%7
        ls+=construct_cal_month(i+1,first_day_of_month,num_days_in_month)+'\n'
    return ls
print construct_cal_year(2000) 



    











def leap_year(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True

def day_of_week_jan1(year):
    return (1+(5*((year-1)%4))+(4*((year-1)%100))+(6*((year-1)%400)))%7
    
def num_days_in_month(month_num,leap_year):
    if month_num==1 or month_num==3 or month_num==5 or month_num==7 or month_num==8 or month_num==10 or month_num==12:
        return 31
    elif month_num==4 or month_num==6 or month_num==9 or month_num==11:
        return 30
    elif month_num==2:
        if leap_year:
            return 29
        else:
            return 28
    else:
        return None    

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    result = []
    if month_num==1:
        result.append("January");
    elif month_num==2:
        result.append("February");
    elif month_num==3:
        result.append("March");
    elif month_num==4:
        result.append("April");
    elif month_num==5:
        result.append("May");
    elif month_num==6:
        result.append("June");
    elif month_num==7:
        result.append("July");
    elif month_num==8:
        result.append("August");
    elif month_num==9:
        result.append("September");
    elif month_num==10:
        result.append("October");
    elif month_num==11:
        result.append("November");
    elif month_num==12:
        result.append("December");
        
    line = " "
    counter = first_day_of_month 
    
    for i in range(counter):
        line+="   " 
    
    for i in range(num_days_in_month):
            line+="%2d" % (i+1) 
            line+=" " 
            counter+=1
            if counter == 7: 
                result.append(line[:-1]) 
                line=" " 
                counter=0 
                
    if line!="": 
        if line[-1]==' ': 
            line=line[:-1] 
        result.append(line)
    
    return result
        
def construct_cal_year(year):
    result=[year]
    for i in range(12):
        first_day_of_month=day_of_week_jan1(year)
        for j in range(i):
            first_day_of_month+=num_days_in_month(j+1,leap_year(year))
        first_day_of_month=first_day_of_month%7
        result.append(construct_cal_month(i+1,first_day_of_month,num_days_in_month(i+1,leap_year(year))))
    return result


def display_calendar(calendar_year):
    retVal=''
    yearCalendar=construct_cal_year(calendar_year)
    month_num=1
    for i in range(12):
        monthCal=yearCalendar[month_num]
        retVal+=monthCal[0]+'\n'
        retVal+="  S  M  T  W  T  F  S\n"
        for lines in monthCal[1:]:
            retVal+=lines+'\n'
        retVal+='\n'
        month_num+=1
    retVal=retVal[:-2]
    return retVal
print display_calendar(2111)