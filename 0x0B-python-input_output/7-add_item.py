#!/usr/bin/python3
""" load add save module """
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
lfjf = __import__('6-load_from_json_file').load_from_json_file

ll = sys.argv[1:]

item = lfjf("add_item.json")
if not item:
    item = []
ans = [*item, *ll]

save_to_json_file(ans, "add_item.json")
