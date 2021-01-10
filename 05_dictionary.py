my_list = ['Robert', 42, 3.14, 'Robert']


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


# add item to dictionary
phonebook["06 20 999 8877"] = {
    "name": "Kiss Krisztina",
    "address": "Eger Fő utca 12."
}

print(phonebook["06 20 999 8877"])

# # delete item
# del phonebook["06 20 999 8877"]
#
# print(phonebook)