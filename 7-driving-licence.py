# The UK driving number is made up from the personal details of the driver. 
# The individual letters and digits can be code using the below information
 
# 1–5: The first five characters of the surname (padded with 9s if less than 5 characters)
# 6: The decade digit from the year of birth (e.g. for 1987 it would be 8)
# 7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)
# 9–10: The date within the month of birth
# 11: The year digit from the year of birth (e.g. for 1987 it would be 7)
# 12–13: The first two initials of the first name and middle name, padded with a 9 if no middle name
# 14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9
# 15–16: Two computer check digits. We will always use "AA"
 
# Your task is to code a UK driving license number using an Array of data. 
# The Array will look like

# data = ["John","James","Smith","01-Jan-2000","M"]
# Where the elements are as follows

# 0 = Forename
# 1 = Middle Name (if any)
# 2 = Surname
# 3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
# 4 = M-Male or F-Female

from dateutil.parser import parse

def driver(data):
      lic = ""
      # 1 to 5
      if len(data[2]) >= 5:
            lic += data[2][:5]
      else:
            lic += data[2]
            while (len(lic) < 5): lic += "9"
      
      # 6
      lic += (str(parse(data[3]).year))[2]

      # 7 to 8
      month = parse(data[3]).month
      if data[4] == "F": month += 50
      month = str(month)
      if len(month) == 1: month = "0" + month
      lic += month

      # 9 to 10
      day = str(parse(data[3]).day)
      if len(day) == 1: day = "0" + day
      lic += day

      # 11
      lic += (str(parse(data[3]).year))[3]

      # 12 to 13
      lic +=  data[0][:1]
      if (data[1]) != "": 
            lic += data[1][:1]
      else:
            lic += "9"

      # 14 to 16
      lic += "9AA" 

      return lic.upper()

print(driver(["John", "James", "Smith", "01-Jan-2000", "M"]))
print(driver(["Johanna", "", "Gibbs", "13-Dec-1981", "F"]))
print(driver(["Andrew", "Robert", "Lee", "02-September-1981", "M"]))

# data = ["John", "James", "Smith", "01-Jan-2000", "M"]
# test.it("Should return SMITH001010JJ9AA")
# test.assert_equals(driver(data), "SMITH001010JJ9AA")

# data = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
# test.it("Should return GIBBS862131J99AA")
# test.assert_equals(driver(data), "GIBBS862131J99AA")

# data = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
# test.it("Should return LEE99809021AR9AA")
# test.assert_equals(driver(data), "LEE99809021AR9AA")