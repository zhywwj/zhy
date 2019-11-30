# Julia day to date

from datetime import datetime

def date():
    J = input('input yearjuliaday: >>')  # input example; 2019001
    date = datetime.strptime(J, '%Y%j')
    print(date)

date()
