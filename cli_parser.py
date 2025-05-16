import re
from commands.show import show
from commands.assign import assign
from commands.add import add
from core.config import command_list
import sys

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
        sys.exit()
    command = re.match(r'^(\w+)', expression).group(1)
    if command == 'show':
        show(expression)
    elif command == 'assign':
        assign(expression)	
    elif command == 'add':
        add(expression)
