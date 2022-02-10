#-------------------------------------------------------------------------------
# Name:        Text_Tab_Replace.py
# Purpose:
# This is a file that will replace the pipe ("|") character with a tab ("\t") character
# in pipe delimited text files that are too larger to manipulate with MS Excel or other
# software packages.
#
# Created:     02/10/2020
# Licence:     public
#-------------------------------------------------------------------------------

## Input and variables
import sys
import os

###################################################################################
# Python program to create a file explorer in Tkinter
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("CSV files","*.csv"),("all files","*.*")))
### Get the TEXT file to update
root.destroy()
###################################################################################

## Variables
in_file = root.filename
wkPath = os.path.dirname(in_file)
in_file_name = os.path.basename(in_file)
out_file_name = in_file_name.replace("txt","tab")
out_file = wkPath + "\\" + out_file_name


## Processing steps
count = 0
fh = open(in_file,'r')
fo = open(out_file,'w')

while True:
    line = fh.readline()
    fo.write(line.replace('|', '\t'))
    count += 1
    if not line:
        break

print(str(count) + " lines processed")
fo.close()
fh.close()