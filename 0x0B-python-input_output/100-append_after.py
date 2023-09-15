#!/usr/bin/python3
"""Search and update file"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+") as file:
        lines = file.readlines()
        updated_lines = []
        for line in lines:
            if search_string in line:
                updated_lines.append(line + new_string)
            else:
                updated_lines.append(line)

        file.seek(0)
        file.writelines(updated_lines)
