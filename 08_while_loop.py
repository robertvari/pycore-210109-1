username = "robert"
password = "testpas123"

your_username = input("Username:")

while your_username != username:
    print("Username is invalid")
    your_username = input("Username:")


your_password = input("Password:")
while your_password != password:
    print("Password is invalid")
    your_password = input("Password:")

print(f"You are logged in {username}.")