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


    pass
    print("Set On Keywords:")
    index = 1
    values = setonlist
    for value in values:
        print('    ',index,')', value)
        index += 1
    print("")
    print("Set Off keywords: ")
    index = 1
    values = setofflist
    for value in values:
        print('    ',index,')', value)
        index += 1
    print("")
    print("Set default keywords:")
    index = 1
    values = setdefaultlist
    for value in values:
        print('    ',index,')', value)
        index += 1


#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    setonlist, setofflist, setdefaultlist=classify_settings(filename)

    #call function to print items in the lists.
    if setonlist or setofflist or setdefaultlist:
        print_settings(setonlist, setofflist, setdefaultlist)
    else:
        print("No settings found on the file.")