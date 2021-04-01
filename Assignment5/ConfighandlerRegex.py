#Author: Naresh Adh
#Date: 03/26/2021
#Through this program, students will learn to:
    #1. validate an input file and contents in it using regular expression.
    #2. Handle file opening in a mode
    #2.1. Handle file exceptions, etc.
    #3. Search file contents
    #4. Use tools to check is a regular expression is 'evil'

import re

#function-1
def classify_settings(filename):
    setonlist = []
    setofflist = []
    setdefaultlist = []
    fd = open(filename, "r")  # open the file to read

    for line in fd:
        if ":" in line:
            configline = line.split(':')
            if re.search("^\s.*true.*,$", configline[1]):
                setonlist.append(re.search("\w*$", configline[0]).group())
            elif re.search("^\s.*false.*,$", configline[1]):
                setofflist.append(re.search("\w*$", configline[0]).group())
            elif re.search("^\s.*default.*", configline[1]):
                setdefaultlist.append(re.search("\w*$", configline[0]).group())

    return setonlist, setofflist, setdefaultlist

#function-2
def  print_settings(setonlist, setofflist, setdefaultlist) :
    print("1) Set On keywords:")
    print('    ',*setonlist, sep='\n    ')
    print("")
    print("2) Set Off keywords:")
    print('    ', *setofflist, sep='\n    ')
    print("")
    print("3) Set default keywords:")
    print('    ', *setdefaultlist, sep='\n    ')

    pass

#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    setonlist, setofflist, setdefaultlist=classify_settings(filename)

    #call function to print items in the lists.
    if setonlist or setofflist or setdefaultlist:
        print_settings(setonlist, setofflist, setdefaultlist)
    else:
        print("No settings found on the file.")