from core.config import command_list, shared_variables

import sys

lines = []
print("Enter lines of text (press Ctrl-D or Ctrl-Z on a new line to end):")
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

# Process the lines
print("You entered:")
for line in lines:
    print(line)