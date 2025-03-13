todo = []
prev_done = []
#to add to the list
def add_item(item):
    todo.append(item)
    return todo

#to view the the list
def view_list():
    for i in todo:
        print(i)