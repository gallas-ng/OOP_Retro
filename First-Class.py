# ------------------- First - Class exemple in python
def search(sequence, expected, finder):
    for elm in sequence:
        if finder(elm) == expected:
            return elm
    raise RuntimeError(f"Could not find {expected}")

friends = [
    {"name" : 'Bob Smith', "age" : 23},
    {"name" : "Fairy Tale", "age" : 110},
    {"name" : "Rolf Hiler", "age" : 21}
]

# def finder(friend):
#     return friend["name"]

search(friends, "Opo", lambda friend: friend["name"])
