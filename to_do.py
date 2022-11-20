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
    if answer == "yes" or answer == "Yes":
        List.append(make_item())
        make_list()
        return List
    else: 
        return List

def print_list(a_list):
    for item in a_list:
        for index in item:         
            print("Task: "  + item[index] + "\nDue Date: " + item[index+1] +"\nTime to complete task: " + item[index+2])
            return item
        item +=1
        return item
        
import re 
def print_text(filename):
    a_list=[]
    with open(filename) as file:
        next(file)
        for line in file: 
            date = line.strip('').split("/")
            print(date, len(date))
            for index in date:
                a_list.append(index)
    for letter in a_list:
        if letter is not str(letter).isalpha():
            print(letter)
    while len(a_list)>0:
        i=0
        day = a_list[i+1]
        event= a_list[i]
        res = re.sub(r'[^a-zA-Z]', '', event)
        a_list.pop(i+2)
        a_list.pop(i+1)
        a_list.pop(i)
        
        
                
    print(a_list)
    print(day, event[0:4])
    print(res)
                



                


def main():
    print_text('tasks.txt')
main()