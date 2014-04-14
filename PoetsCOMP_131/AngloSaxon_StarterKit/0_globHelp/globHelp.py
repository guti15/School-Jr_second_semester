
import glob
import re

def main():
	# input directory (that holds all the files)
	inputDIRECTORY = "test"
	print ("\nFILES in directory: ", inputDIRECTORY)
	
	# ------------ get all (*) FILES in this directory ( test/ )----------------
	fileList = glob.glob(inputDIRECTORY + '/*')
	fileList.sort()
	for nextFile in fileList:
		# open the FILE in this directory
		INPUT = open(nextFile, 'r')
		print ("\t", nextFile)	
		
	
	print ("\nDone.\n\n")
	
# end main() --------------------------------------------------
	

def formatLine(line):
# SUMMARY: (1) remove all punctuation and (2) convert to lowercase
# 
# IN (line): one line of text read from a raw text file
#
# RETURN: same line with formatting completed
#
#-----------------------------------------------------------	
	
	# (1) remove punctuation:
	space = ' '
	# compile (or make) a regular expression (regex)
	puncList = re.compile('[^A-Za-z0-9&;#]')
	# now, substitute a space in each place the regex matches in this line
	newLine = puncList.sub(space, line)
	print(newLine)
	
	# (2) make all words lower case
	newLine = newLine.lower()
		
	return newLine

#--- end formatLine() --------------------------------------------------

#-----------\
# START HERE \
#-----------------------------------------------------------	
if __name__ == '__main__':
	main()

#-----------------------------------------------------
