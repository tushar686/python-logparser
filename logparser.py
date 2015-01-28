from time import sleep
import sys

filename = "./apache_log.log"
linesCount = 1
batchSize = 10
sleepTimeInSeconds = 1

def parseLogFileInbatchSizes():
	with open(filename) as logfile:	
		while(True):
			printNextBatchOfLines(logfile)	
			sleep(sleepTimeInSeconds)

def printNextBatchOfLines(logfile):
			global linesCount	
			global batchSize
			linesCount += 1
			line = "starting"
			print "scanning batch ", (linesCount / batchSize), "-" * 80
			logfile.seek(logfile.tell(), 0)
			while linesCount % batchSize != 0 and line:
				linesCount += 1
				line = logfile.readline()
				if isException(line):					
					print line
					print logfile.readline()
					print logfile.readline()
				
def isException(line):
	if "Exception" in line:
		return True
	return False	
					
			
			
if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	if len(sys.argv) > 2:	
		batchSize = int(sys.argv[2])
	if len(sys.argv) > 3:
		sleepTimeInSeconds = int(sys.argv[3])
	parseLogFileInbatchSizes()
	