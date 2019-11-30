# calculate JuliaDay
from datetime import datetime

def JuliaDay():
    Date = input ("input date year-month-day: >>")
    j = datetime.strptime(Date, '%Y%m%d').timetuple()
    print(j.tm_yday)

JuliaDay()
