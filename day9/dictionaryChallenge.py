# Don't change the code below

travel_log = [
    {
        "country": "France",
        "visits": 11,
        "visited" : ["Paris", "Nice", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 8,
        "visited" : ["Berlin", "Hamburg", "Stuttgard"],
    }
]

# Do not change the code above

# To do
# write the function that will allow new countries to be added

print("\n Before: \n", travel_log)

def add_new_country(country_visited, times_visited, cities_visited):
    travel_log.append({
        "country" : country_visited,
        "visits" : times_visited,
        "visited" : cities_visited
    })


# Do not change code below
add_new_country("Russia", 2, ["Moscow", "Petersburg"])

print("\n After: \n", travel_log)