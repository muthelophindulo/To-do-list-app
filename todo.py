from manipulate_list import *
import time

def app():
    print("..............TO DO LIST APP..............")
    while True:
        time.sleep(0.2)
        print("""
            1. view the to do list
            2. add item
            3. remove item
            4. mark done
            5. view previous done 
                  """)
        time.sleep(0.2)

        inp = int(input("what would you like to do? "))
        match inp:
            case 1:
                view_list()
                time.sleep(0.2)
            case 2:
                item = input("enter item to be added: ")
                add_item(item)
                print()
                time.sleep(0.2)

                print(f"succesfully added {item} on the to do list")

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
                view_list()
                remove()
            
            case 4:
                mark_done()
            
            case 5:
                view_prev_done()
            
            case _:
                print("error")

        cont = input("would you like to continue(y/n)?: ")
        if cont == "y" or cont == "yes":
            continue
        else:
            time.sleep(0.2)
            print("Goodbye")
            break
