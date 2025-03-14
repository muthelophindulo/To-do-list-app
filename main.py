from App import *

print("."*5,"welcome","."*5)
start = input("would you like to open the app?: ")

if start == "yes" or start == "y":
    app()
else:
    print("error")
    option = input("would you like to try again? ")
    if option == "yes" or option == "y":
        app()
    else:
        print("goodbye")
