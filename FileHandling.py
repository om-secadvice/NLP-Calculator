import os
path1 = os.path.dirname(os.path.abspath(__file__))

def add_element(string):
    path = path1 + '/addition.txt'
    addfile = open(path,'r')
    init = addfile.readlines()
    updated = ""
    string += "\n"
    if string not in init:
        addfile = open(path,'r')
        updated = addfile.read()
        updated +=string
        addfile = open(path,'w')
        addfile.write(updated)
    addfile.close()

def test():
    path = path1 + '/addition.txt'
    addfile = open(path,'r')
    init = addfile.readlines()
    print(len(init))	
    l = []
    for w in init:
        l.append(w.strip())
    addfile.close()
    return l

def error(string):
    path = path1 + '/Subtraction.txt'
    subfile = open(path,'r')
    init = subfile.readlines()
    updated = ""
    string += "\n"
    if string not in init:
        subfile = open(path,'r')
        updated = subfile.read()
        updated +=string
        subfile = open(path,'w')
        subfile.write(updated)
    subfile.close()
