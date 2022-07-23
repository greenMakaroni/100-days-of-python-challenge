# Dictionary

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

print("Capitals: ", capitals)

# Nesting list in a dictionary
travel_log = {
    "France": ["Paris", "Nice", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgard"]
}

print("Travel log: ", travel_log)

# Nesting dictionary in a dictionary
nested_log = {
    "France": {
        "visited" : ["Paris", "Nice", "Dijon"],
        "not_visited" : ["Lille"]
    },
    "Germany": {
        "visited" : ["Berlin", "Hamburg", "Stuttgard"],
        "not_visited" : ["Munich"]
    }
}

print("Nested log: ", nested_log)

# Nesting dictionary in a list

travel_log2 = [
    {
        "country": "France",
        "visited" : ["Paris", "Nice", "Dijon"],
        "not_visited" : ["Lille"]
    },
    {
        "country": "Germany",
        "visited" : ["Berlin", "Hamburg", "Stuttgard"],
        "not_visited" : ["Munich"]
    }
]



print("Nesting hell", travel_log2)




