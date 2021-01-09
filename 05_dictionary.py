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

print(
    phonebook["06 30 666 7788"]["name"],
    phonebook["06 30 666 7788"]["address"]
)