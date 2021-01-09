# lists
#           0         1
names = ["Csaba", "Robert", "Csaba"]


# add item
names.append("Csilla")
names.append("Tamás")
names.append("István")
names.append("Kriszta")

print(names)
print(names[-2])

# remove()
names.remove("Csaba")
print(names)

del names[-1]
print(names)

my_name = "Robert Vari"
print(my_name[1])
