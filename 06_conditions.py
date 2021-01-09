age = 10

if age != 10:
    print("You are older than me!")

# if age >= 10:

# if age <= 10:

username = "robert"
password = "testpas123"

your_user = input("username:")
your_password = input("password:")

#           True                      True
if username == your_user and password == your_password:
    print("You are logged in!")
else:
    print("Invalid credentials provided. Try again")

#           False                      True
if username == your_user or password == your_password:
    print("Username or password was invalid but you are logged in anyway...")
else:
    print("Invalid credentials provided. Try again")