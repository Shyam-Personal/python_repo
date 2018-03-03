#!/usr/bin/python

import os

def print_dir(dir_path):
        files = []
        for i in os.listdir(dir_path):
                new_path = os.path.join(dir_path,i)

                if os.path.isdir(new_path):
                        d = print_dir(new_path)
                        if d:
                                files = files + d
                else:
                        files.append(i)
        return files

#dir_name = str(input("Enter the path : "))
s = print_dir("C:\\Users\\cepl-pc\\Desktop")
print(s) 
