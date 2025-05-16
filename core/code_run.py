import re
from config import shared_variables, command_list
from func_registry import functions

def code_run(expression):
    command_pattern = r'(\w+)'
    match = re.match(command_pattern, expression)
    command = match.group(0)
    if command in command_list:
        functions[command](expression)
        
        

code_run('assign 12 to bottles')
code_run('show bottles')