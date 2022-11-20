from calendar_code import MplCalendar
import calendar_code

"""
in this module take the calendar module and import dates into it
""" 
Nov = MplCalendar(2022, 10)
# Nov.add_event()
Nov.show()
import re 
def add_event(filename, Calendar):
    a_list=[]
    with open(filename) as file:
        next(file)
        for line in file: 
            date = line.strip('').split("/")
            print(date, len(date))
            for index in date:
                a_list.append(index)
    # for letter in a_list:
    #     if letter is not str(letter).isalpha():
    #         print(letter)
    while len(a_list)>0:
        i=0
        day = a_list[i+1]
        event= a_list[i]
        res = re.sub(r'[^a-zA-Z]', '', event)
        a_list.pop(i+2)
        a_list.pop(i+1)
        a_list.pop(i)
        Calendar.add_event(day, res)


def main():
    filename = "tasks.txt"
    Nov = MplCalendar(2022, 10)
    add_event(filename, Nov)
    Nov.show()

main()
