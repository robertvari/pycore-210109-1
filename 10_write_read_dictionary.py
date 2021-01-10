import json

phonebook = {
    "06 20 555 6677": {
        "name": "Robert Vari",
        "address": "Debrecen Fo utca 1."
    },

    "06 30 666 7788": {
        "name": "Kiss Csaba",
        "address": "Budapest Petofi utca 1."
    }
}

with open("phonebook.json", "w") as f:
    json.dump(phonebook, f)

with open("phonebook.json") as f:
    phonebook = json.load(f)
    print(phonebook["06 20 555 6677"]["name"])