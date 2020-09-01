#!/usr/bin/python3
import sys
from pprint import pprint
def get_broken_packages(file_name):
    ppa_list = []
    with open(file_name) as file:
        for line in file:
            if "Broken" in line:
                ppa_list.append(line.replace("Broken", "").split(":")[0])
    if not ppa_list:
        return "list is empty"
    else:
        return ppa_list

#ef remove_packages():


if __name__ == "__main__":
    pprint(get_broken_packages(sys.argv[1]))
