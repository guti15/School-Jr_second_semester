
"""
====================================================================
Programmer: Robert Gutierrez

Title:  Uniqueness of words
====================================================================
Summary:
=====================================================
This program creates an Excel (and optional HTML)
report of all the words in Anglo-Saxon poetry that
do *not* occur in the Anglo-Saxon prose.

METHOD:
It first generates a dictionary (hash table) of
all the words in Anglo Saxon Poetry and then
removes words from that dictionary if the word
appears in the Prose. This leaves the dictionary 
holding only those words that appear in poetry alone.

=====================================================
INPUT:


=====================================================
OUTPUT:


====================================================================
Date Last Modified:

1/13/10 -- wrote program to test concept
Eric Drewniak '11 & Christina Nelson '11

03/09/2010 (mdl) - cleaned up code; made Starter Kit
03/10/2010 (mdl) - split up Excel and HTML reports

03/09/2014 (mdl) - updated Starter Kit

04/xx/2014 (xxx) -

====================================================================
"""


#=====================================================

#-----------------------------------------------------
# IMPORTS:

import sys
import os
import time
import decimal
import string
import glob
import re



INPUT_DIR = "large_AngloSaxon_Corpus"
              
#INPUT_DIR   = "testDIR"

POETRY_DIR  = "A_Poetry"

ExcelFileName  = "Gutierrez_a5.csv"      # names of the output file
HTMLfileName   = "Gutierrez_a5.html"

wantHTML = True;    # True creates an html file
                    # False does not create an html file

#-----------------------------------------------------


#-----\
# main \
#-----------------------------------------------------------	
def main():

	dictionary = {}         # instantiate dictionary (to hold all words)
	
	genreList = []          # instantiate list of genres (poetry or prose)
	manuscriptList = []     # instantiate list of manuscripts in poetry
	fileList = []           # instantiate list of files in manuscripts

	
	print ("\n\n")
	
	# -------------------------------------------
	# work our way through the input directories
	#--------------------------------------------
	# glob sorted texts folder into genreList

# ----- My turn to do work here ----- 


        
	genreList = glob.glob(INPUT_DIR + '/*')
	genreList.sort()
	
	for genre in genreList:
		# in Linux, glob() may return the '.' and '..' directories, so
		# check to make sure we are not procesing folder '.' or '..'
		if (genre == "." or genre == ".."):
			continue   # ... to next genre in the genreList
			
		# print current genre (so we know which genre we are working on)
		print (genre)
			

		# ------------ get all MANUSCRIPTS in this genre ----------------

		manuscriptList = glob.glob(genre + '/*')

		manuscriptList.sort()

		for manuscript in manuscriptList:

			# check to make sure we are not procesing folder '.' or '..'
			if (manuscript == "." or manuscript == ".."):
				continue
			
			# print current manuscript 
			print ("\t", manuscript)
					
			# ------------ get all FILES in this manuscript ----------------
			fileList = glob.glob(manuscript + '/*')
			fileList.sort()
			for file in fileList:
				# check to make sure we are not procesing folder '.' or '..'
				if(file == "." or file == ".."):
					continue
							
				# open the FILE in this manuscript
				INPUT = open(file, 'r')
				print ("\t\t", file, "\n")
				
				# read this file, one line at a time
				
				# ------------ foreach LINE in this file ----------------
				for line in INPUT:
					# "chomp" line -> remove endlines
					line = line.rstrip()
					# format line -> remove other unwanted characters
					line = formatLine(line)
								
					# ------ SPLIT line into LIST of individual words
					listOfWords = line.split()
					
					# ------ FOREACH word (one at a time) -----------
					for word in listOfWords:
						
						# CASE 1: we are working on poetry
						#         keep each word in the poetry
						#         and a count of the #times it appears
						if genre == INPUT_DIR + '/' + POETRY_DIR:
							# build dictionary (hashtable) of all words in 
							# poetry and their counts
							if word in dictionary:
								# increment that word's count
								dictionary[word] = dictionary[word] + 1
							else:
								dictionary[word] = 1
								
						# CASE 2: otherwise, we are working on prose
						#         so, if a word appears in prose, we will
						#         DELETE it (so we only keep words *not* in prose)
						else: 
							if word in dictionary:
								#delete word from dictionary
								del dictionary[word]
					# ------ END FOREACH word in this line
							
				# ------------ END foreach LINE in this file
							
				# we're done with this file
				INPUT.close()
							
			# ------------ END foreach FILE in this manuscript
					
		# ------------ END foreach MANUSCRIPT
		
	# ------------END foreach genre
	
	print ("\nDone Reading Texts ...")
	
	print ("\nMaking EXCEL report ...")
	makeExcelReport(dictionary, ExcelFileName)

	if (wantHTML):
		print ("\nMaking HTML report ...")
		makeHTMLReport(dictionary, HTMLfileName)
                
                                
				
	print ("\n\nDone.")



	
	
#----------------\
# makeExcelReport \
#-----------------------------------------------------------	
def makeExcelReport(dictionary, ExcelFileName):
	
	# open outfile pointer
	outfile = open(ExcelFileName, 'w')
	
	# instantiate sorted dictionary to sort words by their counts
	sortedDictionary = {}          
		
	# sort dictionary by values (counts); we'll use the count(value)
	# as the KEY this time; since some words will have the same count,
	# we'll keep words with the same count in a LIST, e.g.,
	# sortedDictionary[13] might hold ["dog", "cat", "foo"], meaning these
	# three words all had counts of 13 instances
	for (word,count) in dictionary.items():
		if count in sortedDictionary:
			sortedDictionary[count].append(word)
		else:   # this is the first time we've seen a word with this count
			# so start a new LIST that contains only this word (so far)
			sortedDictionary[count] = [word]
			
	# print dictionary to file
	outfile.write("Unique Poetry Words and Their Counts\n")
	outfile.write(("Number of words unique to poetry: %d\n\n")%(len(dictionary)))
	
	# print headings in Excel file
	outfile.write("Occurances,Word,Formatted Word\n")
	
	# reverse=True will print counts in descending order
	excelprint = 0 # My COUNT 
                # ----- FOREACH unique count(key) in sortedDictionary -----
        for key in sorted(sortedDictionary, reverse=True):
                        # FOREACH of the words (in the LIST) with this count
                        for word in sortedDictionary[key]:
                                
                                formattedWord = word
                                # perform some anglo-saxon special character conversions
                                formattedWord = formattedWord.replace('&t;','&thorn;')
                                formattedWord = formattedWord.replace('&ae;','&aelig;')
                                formattedWord = formattedWord.replace('&d;','&eth;')
                                formattedWord = formattedWord.replace('&e;','&#275;')
                                if excelprint < 10 :
                                        outfile.write(str(key)+','+word+','+formattedWord+'\n')
                                        excelprint = excelprint +1

                # ---- END foreach word ------
	# ---- END foreach count(key) ------
		
	# close outfile file
	outfile.close()
		
#---------------\
# makeHTMLReport \
#-----------------------------------------------------------	
def makeHTMLReport(dictionary, HTMLfileName):
        
	        

	outfileHTML = open(HTMLfileName, 'w') 

	# instantiate sorted dictionary to sort words by their counts
	sortedDictionary = {}          
		
	# sort dictionary by values (counts)


	#--------------------------------------------------------------
        #lets work with this code :

        htmlPrint = 0 
        		
	# sort dictionary by values (counts); we'll use the count(value)
	# as the KEY this time; since some words will have the same count,
	# we'll keep words with the same count in a LIST, e.g.,
	# sortedDictionary[13] might hold ["dog", "cat", "foo"], meaning these
	# three words all had counts of 13 instances
        outfileHTML.write("<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n<title>Robert_Table</title>")
        outfileHTML.write("<link rel='stylesheet' type='text/css' href='./Table.css'>\n</head>\n<body>")
        outfileHTML.write ("<p><h1>")
	outfileHTML.write("Unique Poetry Words and Their Counts\n")
        outfileHTML.write ("</h1>\n<br>\n")

	for (word,count) in dictionary.items():
		if count in sortedDictionary:
			sortedDictionary[count].append(word)
		else:   # this is the first time we've seen a word with this count
			# so start a new LIST that contains only this word (so far)
			sortedDictionary[count] = [word]
			
	# print dictionary to file
        outfileHTML.write("<h2>")
	outfileHTML.write(("Number of words unique to poetry: %d\n\n")%(len(dictionary)))
        outfileHTML.write("</h2>")
        outfileHTML.write("<h3>Displaying top 3 words</h3>\n")
	# print headings in Excel file
        outfileHTML.write(" <table style='border:solid 1px #0000'> \n <tr>")
	outfileHTML.write("\n<td>Occurances</td> <td>Word</td><td>Formatted Word</td>\n   </tr>")
# ---DeLETE        outfileHTML.write()  # got to move oout
	# reverse=True will print counts in descending order
	
	# ----- FOREACH unique count(key) in sortedDictionary -----
	for key in sorted(sortedDictionary, reverse=True):
		
		# FOREACH of the words (in the LIST) with this count
		for word in sortedDictionary[key]:
			formattedWord = word
			
			# perform some anglo-saxon special character conversions
			formattedWord = formattedWord.replace('&t;','&thorn;')
			formattedWord = formattedWord.replace('&ae;','&aelig;')
			formattedWord = formattedWord.replace('&d;','&eth;')
			formattedWord = formattedWord.replace('&e;','&#275;')
			if htmlPrint < 3: 
                                #outfileHTML.write(str(key)+','+word+','+formattedWord+'\n')
                                outfileHTML.write("<tr> \n <td>") 
                                outfileHTML.write(str(key)+'</td> \n <td>'+word+ '</td> \n <td>'+formattedWord+'</td> \n </tr>')
                                htmlPrint +=1


		
		# ---- END foreach word ------
		
	# ---- END foreach count(key) ------
        outfileHTML.write("</table></body>\n</html>\n")      # close table 
	# close outfile file
        makeCSS(HTMLfileName)

        

        


        #-------------------------------------------------------------
	
	
	# print dictionary to HTML file 	
	
	
#	outfileHTML.write("Sorry, you have to do it!\n")
	
	
	
	
	
	outfileHTML.close()

		
#-----------\
# formatLine \
#-----------------------------------------------------------	
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
	#print (newLine)
	
	# (2) make all words lower case
	newLine = newLine.lower()
		
	return newLine

#--- end formatLine() --------------------------------------------------

def makeCSS(HTMLfileName):
        HTMLfileName = "Table.css"
	outCSSfile = open(HTMLfileName, 'w') 
        outCSSfile.write("tr,td,table{  border: 2px solid black;\ntext-align:center; \n}")
        outCSSfile.write("h1,h2,h3{ text-align: center; \n}")
        outCSSfile.write("*{background-color: #85847F; \n font-family:Helvetica;\n width 50%;\nmargin: 0 auto;\n} \n")

        outCSSfile.close()

#--------------------------------------------------


#-----------\
# START HERE \
#-----------------------------------------------------------	
if __name__ == '__main__':
	main()

#-----------------------------------------------------------
