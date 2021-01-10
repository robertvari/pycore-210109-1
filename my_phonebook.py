import time, json, os

print("=" * 50, "My Phonebook", "=" * 50,)
time.sleep(2)


phonebook = {}

if os.path.exists("phonebook.json"):
    with open("phonebook.json") as f:
        phonebook = json.load(f)

name = input("Name:")
phone = input("Phone:")
address = input("Addres:")

phonebook[phone] = {
    "name": name,
    "address": address
}

print("Saving data to database...")
time.sleep(2)

with open("phonebook.json", "w") as f:
    json.dump(phonebook, f)