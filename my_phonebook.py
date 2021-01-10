import time, json, os

print("=" * 50, "My Phonebook", "=" * 50,)
time.sleep(2)


phonebook = {}


if os.path.exists("phonebook.json"):  # if phonebook.json exists open it
    with open("phonebook.json") as f:  # open .json file
        phonebook = json.load(f)

    # print existing numbers
    print("Existing numbers:")
    for phone_number, data in phonebook.items():
        print(f"\t {data['name']} {phone_number}")



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