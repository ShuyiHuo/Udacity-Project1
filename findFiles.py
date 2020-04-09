#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:20:49 2020

@author: shuyihuo
"""

import os

cwd = os.getcwd()
data_folder = os.path.join(cwd, 'testdir')
path = data_folder

def find_files_helper(suffix, path):
    paths_with_suffix = []
    if os.path.isfile(path) == True:
        if path.endswith(suffix):
            paths_with_suffix += (path)
    else:
        if os.path.isdir(path) == True:
            elements = os.listdir(path) # getting all directories and files in current path
            for e in elements:
                paths_with_suffix += (find_files_helper( suffix, '{}/{}'.format(path,e)))
        else: 
            return "There is no file with path: " + path
                
    string = ''
    for item in paths_with_suffix:      
        string += item
        
    return string

def find_files(suffix, path): 
    string = find_files_helper(suffix, path)
    if string != None and string != "":
       s = string.split(suffix)
       l = []
       for item in s:
           if item !=None and item != '':
              l.append(item+suffix)
       return l
    else: return "There is no file end with " + suffix
        
    
'''
Test part:

'''  

'''
case 1: Test the function if it could find file end with '.c'.

''' 
print(find_files('.c',path))
print('\n')

'''
case 2: Test the function if it could find file which is not end with '>'.
        Expected output is "There is no file end with >" .
'''
print(find_files('>',path))
print('\n')

'''
case 3: Test the function if it could find file with wrong path.
        Expected output is "There is no file with path: no path" .
'''

print(find_files_helper('.c',"no path"))
print('\n')




