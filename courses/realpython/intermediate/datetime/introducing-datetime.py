# time
import time
# time is the epoch
print(time.time())
# Date & Time
import datetime
# create a date
dt1 = datetime.date(year=2012, month=12, day=21)
print(dt1)
# create a time 
dt2 = datetime.time(hour=13, minute=25, second=42)
print(dt2)
# datetime
dt = datetime.datetime(year=2012, month=12, day=21, hour=13, minute=25, second=42)
print(dt)

# today's date
today = datetime.date.today()
print(today)
# something similar in datetime, the now method
now = datetime.datetime.now()
print(now)
# calculate current time with args
when = datetime.time(now.hour, now.minute, now.second)
print(when)
# combine today with when
combined = datetime.datetime.combine(today, when)
print (combined)
#formatted output
then= "12-21-2012 13:25:42"
format_string = "%m-%d-%Y %H:%M:%S"
parse = datetime.datetime.strptime(then, format_string)
print(parse)
print(repr(parse))