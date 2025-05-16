import re
from config import command_list, shared_variables

def assign(expression):
    pattern = command_list['assign']
    match = re.match(pattern, expression)
    user_value = match.group(1)
    user_variable = match.group(3)
    #globals()[user_variable] = user_value
    #print(f"{user_variable} equals {globals()[user_variable]}")
    shared_variables[user_variable] = user_value