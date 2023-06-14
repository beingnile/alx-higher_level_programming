#!/usr/bin/python3
"""Adds all arguments to a Python list then saves them to a file"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Scripts entry point"""
    filename = "add_item.json"
    if not os.path.exists(filename):
        my_list = []
        save_to_json_file(my_list, filename)
    my_list = load_from_json_file(filename)

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    main()
