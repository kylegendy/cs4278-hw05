import sys
import os
import subprocess

# READ IN THE FLAGS
n = int(sys.argv[1])
CONST_COMMAND = "./is-pngtest.sh"

# PRE-FUNCTIONS -- FIND BASE PERCENTAGE
def setup(arr):
    testpng_dirPath = "./libpng/large-png-suite"
    testout_dirPath = "./libpng"
    pngTest_path = "./libpng/deriv"

    # remove deriv directory if present, and then copy a new one
    subprocess.call("rm -rf " + pngTest_path + " && cp -r " + testout_dirPath + "/libpng-1.6.34/ " + pngTest_path, shell=True)

    for i in arr:
        # compile and store data on each png
        subprocess.call(pngTest_path + "/pngtest " + testpng_dirPath + "/" + str(i) + ".png", shell=True)
        print('finished file: ' + str(i))
    
    # get output for the cumulative png file test inputs
    subprocess.call("gcov *.c > " + testout_dirPath + "/gcov_output.txt", shell=True)
    # store percentages png cumulativee
    file = open(testout_dirPath + "/gcov_output.txt")	
    content = file.readlines()
    line = content[64]
    percentage = float(line[15:20])
    file.close()

    # output percentage to accessible file
    file = open("./perc.txt")
    file.write(percentage)
    file.close()

# FUNCTION DEFINITIONS
def reduce(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res

def isInteresting(arr):
    # generate call
    call = CONST_COMMAND
    for i in arr:
        call += " " + str(i)
    # return the message from the call
    return os.system(call)

def DD(P, arr):
    size = len(arr)
    # base cases
    if (size <= 0):
        raise ValueError("size of array cannot be less than or equal to zero")
    elif (size == 1):
        return arr
    
    # partition
    p_index = int(size / 2)
    P_one = arr[0:p_index]
    P_two = arr[p_index:]
    
    # divide and conquer
    if (isInteresting(reduce(P + P_one))):
        return DD(P,P_one)
    elif(isInteresting(reduce(P + P_two))):
        return DD(P, P_two)
    else:
        return DD(reduce(P + P_two), P_one) + DD(reduce(P + P_one), P_two)

# RUN THE SCRIPT
base_arr = list(range(n))
setup(base_arr)
# print(DD([], base_arr))