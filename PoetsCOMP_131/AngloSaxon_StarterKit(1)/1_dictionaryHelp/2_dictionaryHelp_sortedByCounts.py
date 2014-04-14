
def main():
	# initialize a DICTIONARY data structure
	dictionary = {}
	
	file  = "testFile.txt"
	#file  = "JEGP.txt"
	INPUT = open(file, 'r')
	print ("Ok, we opened the file: ", file, "\n")
				
	# read this file, one line at a time
				
	# ------------ foreach LINE in this file ----------------
	for line in INPUT:
		# "chomp" line -> remove endlines
		line = line.rstrip()
					
		# ------ SPLIT the line into a LIST of individual words
		listOfWords = line.split()
					
		# ------ FOREACH word (one at a time) -----------
		for word in listOfWords:
						
			if word in dictionary:
				# increment that word's count
				dictionary[word] = dictionary[word] + 1
			else:
				dictionary[word] = 1
						
		# ------ END FOREACH word in this line
							
	# ------------ END foreach LINE in this file
							
	# we're done with this file
	INPUT.close()
	
	
	# now let's print out the dictionary (word, count) pairs
	#for (word,count) in dictionary.items():	
	#	print ("%s,%d" % (word, count) )
	
	sortedDictionary = {}	
	for (word,count) in dictionary.items():
		if count in sortedDictionary:
			sortedDictionary[count].append(word)
		else:   # this is the first time we've seen a word with this count
			# so start a new LIST that contains only this word (so far)
			sortedDictionary[count] = [word]		

	for key in sorted(sortedDictionary, reverse=True):
					
		# FOREACH of the words (in the LIST) with this count
		for word in sortedDictionary[key]:
			formattedWord = word
			print (key, word)
	
# end main() -----------------------------------------

#-----------\
# START HERE \
#-----------------------------------------------------------	
if __name__ == '__main__':
	main()

#-----------------------------------------------------
