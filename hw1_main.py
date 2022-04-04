import subprocess
import os

testpng_dirPath = "../testFiles"
testout_dirPath = "./testOut"

subprocess.call("sh ./configure CFLAGS=\"--coverage -static\"", shell=True)
subprocess.call("make clean ; make", shell=True)

percs = []

for aFile in os.listdir(testpng_dirPath):
	# compile and store data on each png
	subprocess.call("./pngtest " + testpng_dirPath + "/" + aFile, shell=True)
	subprocess.call("gcov *.c > " + testout_dirPath + "/" + aFile + ".txt", shell=True)
	
	# store percentages for each png
	file = open(testout_dirPath + "/" + aFile + ".txt")	
	content = file.readlines()
	line = content[64]
	percentage = float(line[15:20])
	
	val = [aFile, percentage]
	percs.append(val)	

	print ('finished file: ' + aFile)


# sort pairs by percentage number
percs.sort(reverse=True,key = lambda x: x[1])

# copy the top 60 pngs over to a new folder
subprocess.call("rm -rf ./bestImages", shell=True)
subprocess.call("mkdir bestImages", shell=True)
i = 0
for x in percs:
	if i > 59:
		break
	print x
	subprocess.call("cp " + testpng_dirPath + "/" + x[0] + " ./bestImages", shell=True)
	i += 1

print 'done!'
