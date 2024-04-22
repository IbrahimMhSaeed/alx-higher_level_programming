#!/usr/bin/python3
""" load add save module """
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
lfjf = __import__('6-load_from_json_file').load_from_json_file

ll = sys.argv[1:]

save_to_json_file(ll, "add_item.json")
item = lfjf("add_item.json")
