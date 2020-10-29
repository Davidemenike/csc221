#!/usr/bin/env python3

import os
import re
import argparse

''' Regex search


Author: Chiemela Emenike
'''


def regex_search(folder_path, regex):
    ''' Given a path to a folder, opens all .txt files in a folder and searches for any line
     that match a user-supplied regular expression. Returns all lines that contain the given regular expression.

     Args: folder_path(str): Path to a folder in the file system 
     regex (str): Regular expression (as a string)

     '''

    if not os.path.isdir(folder_path):
        return 'Input a directory path'

    userRegex = re.compile(regex)


    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(filename) as file:
                
                for line in file:
                    mo = userRegex.search(line)

                    if mo:
                        print(line, end= '')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help= 'Folder to search for .txt files')
    parser.add_argument('regex', help='Regular expression to search for ')

    args = parser.parse_args()

    for line in regex_search(args.folder, args.regex):
        print(line)

if __name__ == "__main__":
    main()