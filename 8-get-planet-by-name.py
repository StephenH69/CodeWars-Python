# def get_planet_name(id):
#     # This doesn't work; Fix it!
#     name = ""
#     switch id:
#         case 1: name = "Mercury"
#         case 2: name = "Venus"
#         case 3: name = "Earth"
#         case 4: name = "Mars"
#         case 5: name = "Jupiter"
#         case 6: name = "Saturn"
#         case 7: name = "Uranus"
#         case 8: name = "Neptune"
#     return name

# Test.assert_equals(get_planet_name(2), 'Venus')
# Test.assert_equals(get_planet_name(5), 'Jupiter')
# Test.assert_equals(get_planet_name(3), 'Earth')
# Test.assert_equals(get_planet_name(4), 'Mars')
# Test.assert_equals(get_planet_name(8), 'Neptune')
# Test.assert_equals(get_planet_name(1), 'Mercury')

def get_planet_name(id):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    return planets[id-1]

print(get_planet_name(2))
    

