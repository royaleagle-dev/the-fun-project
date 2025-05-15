import re

command_list = {
	'show': r'show\s+(.*)',
	'add': r'(\w+)\s+([\d,\s]+)',
	'assign': r'assign\s+(\w+)\s+(to)\s+(\w+)'
}

def replace_variable(match):
	variable_name = match.group(1)
	if variable_name in globals():
		return str(globals()[variable_name]) #variable replaced with value.
	else:
		return match.group(0) #if not variable, leave as it is.

def show(expression):
	pattern = command_list['show'];
	match = re.match(pattern, expression)
	if match:
		sentence = match.group(1)
		variable_pattern = r'(\w+)'
		result = re.sub(variable_pattern, replace_variable, sentence)
		print(result)

def main():
	expression = input("Pls input Expression");
	command = re.match(r'^(\w+)', expression).group(1)

	if command == 'show':
		show(expression)
		

	elif command == 'add':
		pattern = command_list['add'];
		match = re.match(pattern, expression)
		numbers = match.group(2)
		numbers = [int(num.strip()) for num in numbers.split(',')]
		total = sum(numbers)
		print(total)

	elif command == 'assign':
		pattern = command_list['assign'];
		match = re.match(pattern, expression)
		user_value = match.group(1)
		user_variable = match.group(3)
		globals()[user_variable] = user_value






