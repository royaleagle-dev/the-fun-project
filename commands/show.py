import re
from core.config import command_list, shared_variables

def replace_variable(match):
    variable_name = match.group(0)
    if variable_name.startswith(("'", '"')) and variable_name.endswith(("'", '"')):
        return variable_name[1:-1]
    if variable_name in shared_variables:
        return shared_variables[variable_name]
    else:
        return match.group(0)

def show(expression):
    pattern = command_list['show']
    match = re.match(pattern, expression)
    if match:
        sentence = match.group(1)
        variable_pattern = r"'[^']*'|\"[^\"]*\"|\b\w+\b"
        result = re.sub(variable_pattern, replace_variable, sentence)
        print(result)