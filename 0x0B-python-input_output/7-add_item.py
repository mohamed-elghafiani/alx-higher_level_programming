#!/usr/bin/python3

"""adds all arguments to a Python list, and then save them to a file
"""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
argv = sys.argv[1:]
data = []
if os.path.isfile(filename):
    data = load_from_json_file(filename)

if argv:
    for arg in argv:
        data.append(arg)
save_to_json_file(data, filename)
