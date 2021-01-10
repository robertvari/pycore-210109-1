name = "\nRobert"

# f = open("my_data.txt", "a")
# f.write(name)
# f.close()

# write file
with open("my_data.txt", "a") as f:
    f.write(name)

# read file
with open("my_data.txt") as f:
    print(f.read())
