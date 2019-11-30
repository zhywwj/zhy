# calculate JuliaDay
from datetime import datetime

def JuliaDay():
    Date = input ("input date year-month-day: >>")   # input example 20190101
    j = datetime.strptime(Date, '%Y%m%d').timetuple()
    print(j.tm_yday)

JuliaDay()
