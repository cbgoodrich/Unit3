#Charlie Goodrich
#10/04/17
#fri13.py - gives you the next 10 friday the 13ths

from calendar import weekday

fri13Counter = 0
i = 0
k = 0
year = date.today().year
month = date.today().month
day = date.today().month
year = 2017
month = 10
day = 13
while fri13Counter < 10:
    if weekday(year, month, day) == 5 and day == 13:
        print(month + "/" + day + "/" + year)
    
    
