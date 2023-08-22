travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(name, counts, cities):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = counts
    new_country["cities"] = cities
    travel_log.append(new_country)

add_new_country("Vietnam", 1, ["Saigon","Danang","Phu Quoc"])

print(travel_log)


