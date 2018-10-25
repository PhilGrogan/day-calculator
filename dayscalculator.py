# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:25:11 2018

@author: gpgrogan763
"""
import datetime
current_year = int(datetime.datetime.now().strftime("%Y"))
current_month =int( datetime.datetime.now().strftime("%m"))
current_day = int(datetime.datetime.now().strftime("%d"))
day_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_years = []
for x in range(1904, current_year, 4):
    leap_years.append(x)
years_of_leap = 0
days = 0

print(f"The current date is {current_year}/{current_month}/{current_day}")
print("Enter your birthday and I will tell you how many days old you are.")

birth_year = int(input("what year were you born: "))
birth_month = int(input("what month (numeric) were you born: "))
birth_day = int(input("what day of the month were you born: "))

for d in range(birth_day, day_months[birth_month - 1]):
    days += 1
if birth_month < 12:
    for month in range(birth_month, 12):
        days += day_months[month]
for year in range(birth_year + 1, current_year):
    days += 365
for month in range(current_month - 1):
    days += day_months[month]
if birth_year in leap_years and birth_month <= 2:
    for year in range(birth_year, current_year):
        if year in leap_years: 
            days += 1
else:
    for year in range(birth_year + 1, current_year):
        if year in leap_years: 
            days += 1
days += current_day
print(f"You are {days:,d} days old.")