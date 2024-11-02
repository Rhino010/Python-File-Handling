"""
1. Exploring Python's OS Module
Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories 
in a given directory. Your script should prompt the user for the directory path and then display the contents.

Code Example:
    import os

    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
Expected Outcome: The script should correctly list all files and subdirectories 
in the specified directory. Handle exceptions for invalid paths or inaccessible directories.
"""

import os


def list_directory_contents(path = 'my_files'):
    for root, dir, file in os.walk(path):
        print("Root: ",root)
        print("Directory: ",dir)
        print("Files: ", file)


list_directory_contents()