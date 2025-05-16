import re
from commands.show import show
from commands.assign import assign
from config import command_list

flag = False
expression = ''



def main():
    expression = input()
    if expression == 'start':
        flag = True
    while flag == True:
        start_program()


def start_program():
    expression = input("Pls input Expression\n")
    if expression == 'stop':
        flag = False
    command = re.match(r'^(\w+)', expression).group(1)
    if command == 'show':
        show(expression)
    elif command == 'assign':
        assign(expression)	
    elif command == 'add':
        pattern = command_list['add'];
        match = re.match(pattern, expression)
        numbers = match.group(2)
        numbers = [int(num.strip()) for num in numbers.split(',')]
        total = sum(numbers)
        print(total)
