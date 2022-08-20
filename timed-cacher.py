import datetime
isMonday = datetime.date.today().isoweekday() == 1

if isMonday == True:
    # a new week begins
    ...