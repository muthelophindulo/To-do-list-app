#imports
from manipulate_list import *
import time
import sqlite3
import pandas as pd
from database import view

#class for the application
class application:
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
        return [item, inp]




#class for the database  
#class database:
    #create a database funtion

    def database():
        global item
        global imp
        #create a connection for the database
        #and connect to the database
        connection = sqlite3.connect('test.db') #using test.db for testing if the code works or not

        #create a cursor
        cur = connection.cursor() #used to add things to the database

        #create a table in the database 
        cur.execute('''CREATE TABLE IF NOT EXISTS item(
                    
                    item TEXT NOT NULL)
                    ''')

        #to insert values in the database
        cur.execute('''INSERT INTO item (item)
                    VALUES(?)''',(item,))
         
        #commit all the changes
        connection.commit()

        #close the connection
        connection.close()

data = application.app()
item = data[0]
imp = data[1]


print(item,imp)
