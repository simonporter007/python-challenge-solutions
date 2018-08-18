import datetime

# No chance I ever would have spotted this without Google
# February has 29 days, therefore it is a leap year, get list of leap years matching calendar
# Clue suggests "tomorrow"
tomorrow = "27th Janaury"
years = [x for x in range(1016, 1996, 20)
         if datetime.date(x, 1, 1).weekday() == 3]
# Clue suggests "second youngest"
print("%s %s" % (tomorrow, years[len(years)-2]))
