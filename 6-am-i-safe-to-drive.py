# Your task is to write a kata that will work out if you are safe to drive! 
# You will be given some alcoholic drinks, a time when you stopped drinking 
# and the time you would like to drive.
# You will need to return the total units (to 2 decimal places) 
# of the alcoholic drinks and a boolean value true if you are able 
# to drive or false if you are still unable to drive.

# Create a method called drive that takes an array of drinks in the format [[strength, volume]] 
# a time when you finished drinking and a time when you would like to drive.
# eg. drive([[10.0,100]], "20:00", "21:00") and it must return [1.0, false]
# Rules
# 1. On average it takes a person 1 hour for their body to remove 1 unit of alcohol.
# 2. Units of alcohol are calculated by strength (ABV) x volume (ml) / 1000 = units. 
# 3. Data passed will be in the format ([[strength,volume]], finished, drive_time). 
# Where finished is the time you stopped drinking and drive_time is the time you would like to drive.
# 4. If the finished >= drive_time then you can assume that it is the next day.
# 5. Times are passed as strings and are in 24 hour format.
# 6. Return total units to 2 decimal places rounded. For example 1.10 => 1.1 
# and 1.236 => 1.24
# 7. Return true if you are able to drive and false if you are not.
# Example
# alcohol = [[5.2,568],[5.2,568],[5.2,568],[12.0,175],[12.0,175],[12.0,175]]
# drive(alcohol, "23:00", "08:15")

from datetime import datetime, timedelta

def drive(drinks, finished, drive_time):
    unitsOfAlcohol = 0
    FMT = '%H:%M'
    returnList = []
    for i in drinks:
        unitsOfAlcohol += ((i[0] * i[1])/1000)
    returnList.append(round(unitsOfAlcohol, 2))
    minutesForAlcohol = unitsOfAlcohol * 60

    timeToDrive = datetime.strptime(drive_time, FMT) - datetime.strptime(finished, FMT)
    if timeToDrive.days < 0:
        timeToDrive = timedelta(days=0,
                seconds=timeToDrive.seconds, microseconds=timeToDrive.microseconds)
    (h, m, s) = str(timeToDrive).split(':')
    minutes = int(h)*60 + int(m) + (int(s)/60)

    if minutesForAlcohol >= minutes:
        returnList.append(False)
    else:
        returnList.append(True)
    return returnList


alcohol = [[5.2,568],[12.0,175]]
print(drive(alcohol, "16:00", "23:00"))

alcohol = [[5.2,568],[5.2,568],[5.2,568],[12.0,175],[12.0,175],[12.0,175]]
print(drive(alcohol, "23:00", "08:15"))

alcohol = [[15.5,568]]
print(drive(alcohol, "23:00", "06:45"))

alcohol = [[10.0,100]]
print(drive(alcohol, "20:00", "21:00"))

alcohol = [[10.0,100]]
print(drive(alcohol, "20:00", "21:01"))



# test.it("Should return '[5.05, True]'")
# alcohol = [[5.2,568],[12.0,175]]
# test.assert_equals(drive(alcohol, "16:00", "23:00"), [5.05, True])

# test.it("Should return '[15.16, False]'")
# alcohol = [[5.2,568],[5.2,568],[5.2,568],[12.0,175],[12.0,175],[12.0,175]]
# test.assert_equals(drive(alcohol, "23:00", "08:15"), [15.16, False])

# test.it("Should return '[8.8, False]'")
# alcohol = [[15.5,568]]
# test.assert_equals(drive(alcohol, "23:00", "06:45"), [8.8, False])

# test.it("Should return '[1.0, False]'")
# alcohol = [[10.0,100]]
# test.assert_equals(drive(alcohol, "20:00", "21:00"), [1.0, False])

# test.it("Should return '[1.0, True]'")
# alcohol = [[10.0,100]]
# test.assert_equals(drive(alcohol, "20:00", "21:01"), [1.0, True])