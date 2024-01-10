#!/usr/bin/python3
import datetime

# print the smallest number of years
print("The Smallest Number Of Years Is: ", datetime.MINYEAR)
# print the biggest number of years
print("Thr Biggest Number Of Years Is: ", datetime.MAXYEAR)
print("=" * 50)
# ------------------------------------------------------------------------------------------------------------------
# That will print the current date so if saw that code in 2030-07-20 that will be your output
date = datetime.date.today()
print(date)
print("=" * 50)
# -----------------------------------------------------------------------------------------------------------------
# that will print the time in hours, mins, secs
t = datetime.time(23, 55, 30)
print("Hours", t.hour)
print("Mins", t.minute)
print("Secs", t.second)
print("=" * 50)
# -------------------------------------------------------------------------------------------------------------------
# that will print date and time but not now
dt = datetime.datetime(24, 12, 2, 23, 55, 30)
print("Years:", dt.year)
print("Months:", dt.month)
print("Days:", dt.day)
print("Hours:", dt.hour)
print("Minutes", dt.minute)
print("Seconds", dt.second)
print("=" * 50)
# ------------------------------------------------------------------------------------------------------------------------
# to print the current date and time:
now = datetime.datetime.now()
print("Current Date & Time: ", now)
print("=" * 50)
# --------------------------------------------------------------------------------------------------------------------------
# That will print difference from two dates and time
dt1 = datetime.datetime(24, 12, 5, 23, 57, 58)
dt2 = datetime.datetime(23, 5, 6, 22, 6, 15)
delta = dt2 - dt1
print(delta)
print("total seconds between the dates", delta.total_seconds())
#----------------------------------------------------------------------------------------------------------------------------