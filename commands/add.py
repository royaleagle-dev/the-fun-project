import re
from core.config import command_list, shared_variables

def add(expression):
    pattern = command_list['add']
    match = re.match(pattern, expression)
    numbers = match.group(2)
    numbers = [int(num.strip()) for num in numbers.split(',')]
    total = sum(numbers)
    print(total)