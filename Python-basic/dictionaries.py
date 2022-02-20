
"""
Add some information ob dictionary and remove one position
"""

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

"""
Add info about Jake in "phonebook" dictionary
"""

phonebook.update({"Jake": 938273443})
print(phonebook)

"""
Remove info about Jake from dictionary
"""

del phonebook["Jill"]
print(phonebook)