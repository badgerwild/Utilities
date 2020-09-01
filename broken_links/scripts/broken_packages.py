#!/usr/bin/python3
import sys
import os
import re
from pprint import pprint
FAIL = '/var/log/dist-upgrade/apt.log'
SOURCE = '/etc/apt/sources.list.d'

def get_broken_packages(file_name):
    ppa_list = []
    with open(file_name) as file:
        for line in file:
            if "Broken" in line:
                ppa_list.append(line.replace("Broken", "").split(":")[0])
    if not ppa_list:
        return "list is empty"
    else:
        ppa_list.sort()
        return ppa_list

def get_ppas(dir_name):
    ppa_source = []
    for dirpath, dirnames, filename in os.walk(dir_name):
        print(dirpath)
        for files in filename:
             with open(dirpath + "/" + files) as f:
                for line in f.readlines():
                    str_process = ''.join(re.findall('https?.*', ''.join(line).strip()))
                    ppa_source.append(str_process.split(" ")[0])
    return set(ppa_source)

if __name__ == "__main__":
    print(get_broken_packages(FAIL))
    print('********************************************************************')
    print(get_ppas(SOURCE))
