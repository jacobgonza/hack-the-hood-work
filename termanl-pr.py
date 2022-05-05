'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# Create our Checklist
from operator import index


checklist = []

# Define Functions
def create(item):
    checklist.append(item)

    return print( f"{checklist[index]} was added to the checklist: {checklist}")

def read(index):
    return print(f"{checklist[index]} is at the {index} position")

def update(index, item):
    checklist.extend(index)
    old_item = checklist[index]

    return print(f"{old_item} was changed to {item}")

def destroy(index):
    old_item = checklist[index]
    checklist.pop(index)

    return print(f"{old_item} was deleted from checklist")

def mark_completed(index):
    checklist.insert(index)

#def list_all_items():
    # List all items code here

#def user_input(prompt):
    # Get user input here

def select(function_code):
    if function_code == "C":
        input_item = input("Enter an element to add to the list: ")
        create(input_item)
        running = True

        return running

    if function_code == "M":
        input_item = input("what would you like to mark off ")
        mark_completed(input_item)
        print(mark_completed, input)
        running = True

        return running

    elif function_code == "R":
        input_item = input("Enter the index postion you are trying to acces in the list: ")
        read(int(input_item))
        running = True

        return running

    elif function_code == "U":
        input_index = input("Enter the index position you are trying to update in the list: ")
        input_item = input("Enter the element you are trying to update to the list: ")
        update(int(input_index), input_item)
        running = True

        return running

    elif function_code == "D":
        input_index = input("Enter the index position of the element you want to delete: ")
        destroy(int(input_index))
        running = True

        return running


running = True

while running:
    selection = input(
        "Press C to add to list, R to Read from list, U to update an existing entry, D to delete an alameny in the list, P to display list, and Q to quit"
        ).upper()
    running = select(selection)