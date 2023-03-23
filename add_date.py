import datetime

current_date = "12/6/20"
current_date_temp = datetime.datetime.strptime(current_date, "%m/%d/%y")
newdate = current_date_temp + datetime.timedelta(days=5)

print(newdate)