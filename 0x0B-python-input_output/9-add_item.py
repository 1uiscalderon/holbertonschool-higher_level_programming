#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
if __name__ == "__main__":
    import json
    from sys import argv
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

    try:
        list_r = load_from_json_file('add_item.json')
    except:
        list_r = []
    for arg in argv[1:]:
        list_r.append(arg)
    save_to_json_file(list_r, "add_item.json")
