# Create Phone Number
# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# createPhoneNumber([1,2,3,4,5,6,7,8,9,0]); // => returns "(123) 456-7890"


def create_phone_number(n):
    str_output = "("
    x = 1
    while x < 13:
        if x < 4:
            str_output = str_output + str(n[x-1])
        elif x == 4:
            str_output = str_output + ") "
        elif x > 4 and x < 8:
             str_output = str_output + str(n[x-2])
        elif x == 8:
            str_output = str_output + "-"
        elif x > 8 and x < 13:
             str_output = str_output + str(n[x-3])
        x += 1
    return str_output

def create_phone_number2(n):
      return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(str(create_phone_number([1,2,3,4,5,6,7,8,9,0])))
print(str(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])))
print(str(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
print(str(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])))
print(str(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])))

print(str(create_phone_number2([1,2,3,4,5,6,7,8,9,0])))
print(str(create_phone_number2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])))
print(str(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
print(str(create_phone_number2([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])))
print(str(create_phone_number2([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])))