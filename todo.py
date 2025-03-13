from manipulate_list import *

def run():
    print("........TO DO LIST APP.........")
    while True:

        print("""
            1. view the to do list
            2. add item
            3. remove item
            4. mark done
            5. view previous done 
                  """)

        inp = int(input("what would you like to do? "))
        match inp:
            case 1:
                view_list()
            case 2:
                item = input("enter item to be added: ")
                add_item(item)
                print()

                print(f"succesfully added {inp} on the to do list")
                while True:
                    continuity = input("would you like to add another item?(y/n): ")
                    if continuity == "y":
                        item = input("enter item to be added: ")
                        add_item(item)
                        print()
                        print(f"succesfully added {inp} on the to do list") 
                    else:
                        break           
            case 3:
                pass
            
            case 4:
                pass
            
            case 5:
                pass
            
            case _:
                print("error")

        cont = input("would you like to continue(y/n)?: ")
        if cont == "y" or cont == "yes":
            continue
        else:
            print("Goodbye")
            break