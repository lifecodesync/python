# 9. Check whether a city entered by the user exists in the list
cities = ["Mumbai", "Pune", "Delhi", "Kolhapur", "Bengaluru"]
city = input("Enter city name: ")
if city.strip().title() in cities:
    print(city, "exists in the list")
else:
    print(city, "does not exist in the list")
