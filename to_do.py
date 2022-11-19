"""
This code provides a viewable to-do list based off user input every morning
"""

#functions needed: request input, print function, pop function

#first function request input to create list item: name of todo, due date/time, time to complete

def make_item():
    item = []
    item.append(input("Please enter a task: "))
    item.append(input("Enter when you would like this task to be completed: "))
    item.append(input("How long will this task take you to complete: "))
   
    return item

def make_list():
    List = []
    answer = input("Would you like to add an item to the list? ")
    if answer == "yes":
        List.append(make_item())
        make_list()
        return List
    else: 
        return List




def main():
    print(make_list())
main()