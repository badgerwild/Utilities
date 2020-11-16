#!/usr/bin/env python3
"""
Script to remove spaces, and conver powerpoint files into zip
files so that I can contro the audio speed
"""

import os
import argparse
import shutil

NEW_LOCATION = ''
NEW_LOCATION_ZIP = ''


def remove_spaces(file_name):
    """
    removes spaces in file name
    """
    name = file_name.replace(" ", "_")
    os.rename(file_name, NEW_LOCATION+'/'+name)
    print(f"{file_name} has been renamed to {name}")
    cp_name = name.replace(".pptx", ".zip")
    shutil.copy(NEW_LOCATION+'/'+name, NEW_LOCATION_ZIP+'/'+cp_name)


if __name__ == "__main__":

    the_parser = argparse.ArgumentParser(description='List contents'
                                         + 'or positonal arguments')

    the_parser.add_argument('File')
    args = the_parser.parse_args()
    the_file = args.File
    remove_spaces(the_file)
