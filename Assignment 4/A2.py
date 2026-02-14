with open('test.txt', 'r') as file:
    cities = file.readlines()

cities = [city.strip() for city in cities]
cities.sort()

for city in cities:
    print(city)