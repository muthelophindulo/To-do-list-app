from todo import *

print("."*5,"welcome","."*5)
start = input("would you like to open the app?: ")

if start == "yes" or start == "y":
    run()
else:
    print("error")