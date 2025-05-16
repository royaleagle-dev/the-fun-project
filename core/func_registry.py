from import_utils import add_project_root_to_path

add_project_root_to_path()

from commands.show import show
from commands.assign import assign
from commands.add import add

functions = {
    "show": show,
    "assign": assign,
    "add": add,
}