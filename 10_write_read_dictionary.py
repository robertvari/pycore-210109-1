phonebook = {
    "06 20 555 6677": {
        "name": "Robert Vari",
        "address": "Debrecen Fő utca 1."
    },

    "06 30 666 7788": {
        "name": "Kiss Csaba",
        "address": "Budapest Petőfi utca 1."
    }
}

with open("phonebook.txt", "w") as f:
    f.write(phonebook)