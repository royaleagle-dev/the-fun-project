# utils.py
import sys
import os

def add_project_root_to_path(levels_up=1):
    """
    Adds the project root folder to sys.path.
    `levels_up` specifies how many levels up from the current file to go.
    Defaults to 1 (parent folder).
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = current_dir
    for _ in range(levels_up):
        project_root = os.path.dirname(project_root)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
