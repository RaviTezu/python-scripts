#!/usr/bin/python
from __future__ import print_function
import datetime as dt

print("How to add 1 hour to current time?")
print(dt.datetime.now() + dt.timedelta(hours=1))
print("\n")
print("How to substract 1 hour 30min from current time?")
print(dt.datetime.now() + dt.timedelta(hours=1, minutes=30))
print("\n")
print("How to substract 1 day from current time?")
dt.datetime.now() - dt.timedelta(days=1)
