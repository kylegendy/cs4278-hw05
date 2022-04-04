import sys
import os

# READ IN THE FLAGS
n = int(sys.argv[1])
CONST_COMMAND = str(sys.argv[2])
for i in sys.argv[3::]:
    CONST_COMMAND += " "
    CONST_COMMAND += str(i)

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
print(DD([], base_arr))