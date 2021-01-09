names = ["Csaba", "Robert", "Kriszta", "Csilla"]

# for loop
for item in names:
    if item == "Kriszta":
        break

    print(item)

for item in names:
    if item == "Kriszta":
        continue
    print(item)

print("End of code!")