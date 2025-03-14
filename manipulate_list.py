todo = ["Go to school","Do washing","Write your homeworks"]
prev_done = []
#to add to the list
def add_item(item):
    todo.append(item)
    return todo

#to view the the list
def view_list():
    n = 1
    for i in todo:
        print(n,i)
        n +=1

#mark done
def mark_done():
    n = 1
    for i in todo:
        print(n,i)
        n +=1

    mark_d = int(input("which item would you like to mark done? "))
    todo.pop(mark_d-1)
    prev_done.append(todo[mark_d-1])
    print(f"succecsfully removed {todo[mark_d-1]}")
    
#view prev_done
def view_prev_done():
    n = 1
    for i in prev_done:
        print(n,i)
        n +=1

#to remove an item
def remove():
    index = int(input("which item would you like to remove?: "))
    todo.pop(index-1)
    print(f"succesfully removed {todo[index-1]}")
