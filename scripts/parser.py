import fileinput
import re
import sys 

try:
    startTime = float(sys.argv[2])
    endTime = float(sys.argv[3])
except ValueError:
    startTime = 0
    endtime = 1000

for line in fileinput.input(sys.argv[1]):
	line = re.sub(r'\[INFO\] \[WallTime: (.*)\] \[(.*)\] (.*)', r'\2 \3', line.rstrip())
   	timeStamp = float(re.sub(r'(.*) (.*)', r'\1', line.rstrip()))
	if (timeStamp > startTime and timeStamp < endTime):
		print(line) 
