import json
import numpy as np
import ast
"""
Given a file which contains memory addresses in each line,
this function generates an offset file.
"""
def generate_offset_file(fileName):
    offsetName = fileName + "_offset.txt"
    offsetFile = open(offsetName,"w")
    with open (fileName+".txt","r") as f:
        lines = f.readlines()
        lines = [line.rstrip().strip() for line in lines]

    # Calculating offsets
    for i in range(len(lines)):
        if i == 0:
            offsetFile.write("0"+"\n")
        elif lines[i]!="0" and lines[i-1]!="0":
            diff = int(lines[i],base=16) - int(lines[i-1],base=16)
            offsetFile.write(str(diff)+"\n")
    offsetFile.close()


"""
Given the offset file and a length, this function generates
a file containing all offset windows of given length.
"""
def generate_windows(fileName):
    windows_list =[]
    with open (fileName+".txt","r") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    
    for i in range(0, len(lines)-7):
        window = lines[i:i+7]
        windows_list.append(window)

    windowsFile = open(fileName+"_windows.txt","w")
    windowsFile.write(json.dumps(windows_list))



def compare_windows2(file1, file2):
    with open (file1,"r") as f:
        str1 = f.read()
    list1 = ast.literal_eval(str1)
    with open (file2,"r") as f:
        str2 = f.read()
    list2 = ast.literal_eval(str2)
    common_elements = np.intersect1d(list1, list2)
    similarity = (len(common_elements)/max(len(list1),len(list2)))*100
    print("%", similarity,"of windows are same between two files.")
    
def compare_windows(file1, file2):
    with open (file1,"r") as f:
        str1 = f.read()
    list1 = ast.literal_eval(str1)
    with open (file2,"r") as f:
        str2 = f.read()
    list2 = ast.literal_eval(str2)
    
    set1=set(tuple(x) for x in list1)
    common_elements = set1.intersection(set(tuple(x) for x in list2))
    similarity = (len(common_elements)/max(len(list1),len(list2)))*100
    print("%", similarity,"of windows are same between two files.")

#generate_offset_file("invalid0")
#generate_windows("invalid0_offset")
compare_windows2("valid0_offset_windows.txt","invalid0_offset_windows.txt")
