"""
----------------------------------------------------------------
Programmer:	ROBERT GUTIERREZ

Summary: This program makes 4 different types of copies of what ever poem you type in the 'FileName' variable.  (0) Lines backwards (1)Randomized (2)Lines Backwards as well as reading the strings backwards (3) The poem is reversed and the words are spelled back completely backwards ex. main == niam, purpose to find palindromes quicker or hidden messages. Hence, this program was built using Python 2.7 

Date last modified: 
 02/25/2014 (mdl) -- Polished up a bit
 02/24/2014 (mdl) -- did my personal function that scrambles it up
 02/23/2014 (mdl) -- did backward lines 
 02/21/2014 (mdl) -- finished the first function and pondered about backward lines


----------------------------------------------------------------

--------------------------------------------------------------
INPUT: 	A poem from a local text (.txt) file. Each input
        file must follow this format: 
        ------------------------------
        | FileName variable must be set to file (poem) name include extension
     
     
OUTPUT: Prints messages to the console and produces new files
        that have deformed the poem in various ways.
        
        Backwards lines:
        The new filename will have "linesBackwards_" prepended to 
        the original filename. For example, an original input
        filename of "maryPoem.txt" will produce a new file called:
        "linesBackward_maryPoem.txt" (in the same directory).


        Randomize Lines: 
        Makes a copy of the poem inputed called Words Backwards_(poem name)
        which contains the lines of the poem in diffrent order, in this ersion the line of the stanza is lost. 

       Words Backwards: 
       This creates the poem in a reverse traversal form of the poem where the reader gets to read the poem from last line starting from the right to left, however the poem is set up so it is easier in the eyes and do not have to do all that work, so the user can continue to read from left to right from top to bottom (traditionally) , punctutaion has been eliminated, and made all lowercase words.

      My Deform: 
      I decided to deform my poem by reversing the lines so top is bottom and then read the words backwards, where even there spelling is backwards to find quicker palindromes or see any hidden message that could possibly be encrypted. File name under : Spell_Backwards_Reverse_(poem name).txt.
Punctutaion has been eliminated, and made all lowercase words.
---------------------------------------------------------------
"""

# import these modules to help me
import re
import codecs
import string
from random import shuffle

def main():
    
    poemFileName = "maryPoem.txt"
    
    print ("")  # blank line
    
    #(1) 
    print ("(1) Starting Reading Lines Backwards ...\n")
    readingLinesBackwards( poemFileName )
    
    #(2)
    print ("(2) Starting Randomize Lines Backwards ...\n")
    randomizeLines( poemFileName )
    
    #(3)
    print ("(3) Starting Reading Words Backwards ...\n")
    readingWordsBackwards( poemFileName )
    
    #(4)
    print ("(4) Starting Reading last two words ...\n")
    
    print ("*** Copies made in current Directory *** \n")

    print ("\nDone.\n")

# end main()
#---------------------------------------------------------

#-----------------------\
# readingLinesBackwards  \
#---------------------------------------------------------
# This function accepts a filename as an argument
# of a (raw) text file that contains lines of a poem.
# The function reverses the lines of the poem and
# outputs the backward poem to a new file. The new
# filename will have "backwards_" prepended to the name.
#
# Each line# of the original poem will be printed to the 
# beginning of each line in the backwards poem, thus the 
# new file will have decreasing line numbers.
#---------------------------------------------------------
def readingLinesBackwards( poemFileName ):
    #this functions flips the poem upside down, and begin reading bottom lines.
    
    INPUT = open(poemFileName, 'r')
    
    newFileName = "linesBackwards_" + poemFileName
    OUTPUT = open(newFileName, 'w')

    # make an empty list to hold all the lines of a poem
    allLines = []
    
    poemTitle  = INPUT.readline().strip()
    poemAuthor = INPUT.readline().strip()
    
    # skip blank line after the author name
    INPUT.readline()
    
    # now read each line of the poem and store the lines in a list
    for nextLine in INPUT:
        nextLine.strip()
        if (nextLine != ""):
            allLines.append(nextLine)
    
    # close the input (original) file
    INPUT.close()
    
    # now reverse the lines in the list
    allLines.reverse()
    
    # get the total number of lines in this poem
    totalLines = len(allLines)
    
    # print title and author
    OUTPUT.write("Lines Backwards\n")
    OUTPUT.write('Title:  {0}\n'.format( poemTitle ))
    OUTPUT.write('Author: {0}\n\n'.format( poemAuthor ))
    
    # i will start counting at the end
    i = totalLines
    
    for line in allLines:
        OUTPUT.write('{0}  {1}\n'.format(i,line) )
        i = i-1
    # end of for loop
    
    OUTPUT.close()  
    
# end readingLinesBackwards()
#---------------------------------------------------------


#----------------\
# randomizeLines  \
#---------------------------------------------------------
# This function makes it possible to read the poem with random line order (stanzas), 
#therefore there is no specific line structre from original poem.
#---------------------------------------------------------
def randomizeLines( poemFileName ):
    
    
    INPUT = open(poemFileName, 'r')
    
    newFileName = "Randomize Lines Backwards_" + poemFileName
    OUTPUT = open(newFileName, 'w')

    # make an empty list to hold all the lines of a poem
    allLines = []
    
    poemTitle  = INPUT.readline().strip()
    poemAuthor = INPUT.readline().strip()
    
    # skip blank line after the author name
    INPUT.readline()
    
    # now read each line of the poem and store the lines in a list
    for nextLine in INPUT:
        nextLine.strip()
        if (nextLine != ""):
            allLines.append(nextLine)
    
    # close the input (original) file
    INPUT.close()
    # from here on out I need to call each cell index randomize word and
    # print the word 
 
    shuffle(allLines)
    
    totalLines = len(allLines)
    
    # print title and author
    OUTPUT.write("Random Lines\n")
    OUTPUT.write('Title:  {0}\n'.format( poemTitle ))
    OUTPUT.write('Author: {0}\n\n'.format( poemAuthor ))
    
    # i will start counting at the end
    i = totalLines
    
    for line in allLines:
        OUTPUT.write(line)
    
    # end of for loop
    
    OUTPUT.close()  
     
    
# end randomizeLines()
#---------------------------------------------------------
    
    
#-----------------------\
# readingWordsBackwards  \
#---------------------------------------------------------
# this function make it possible to read the poem Backwards reading from right to left
# the poem begins from the bottom as well.  if do not intend  to read like that suggest removing 
# allLines.reverse() in line 242. 
#---------------------------------------------------------
def readingWordsBackwards( poemFileName ):
   
    
    # INPUT = open(poemFileName, 'r')
    
    #---------------------------------------------------------------

        
    INPUT = open(poemFileName, 'r')
    
    newFileName = "Words Backward_" + poemFileName
    OUTPUT = open(newFileName, 'w')

    # make an empty list to hold all the lines of a poem
    allLines = []
    
    poemTitle  = INPUT.readline().strip()
    poemAuthor = INPUT.readline().strip()
    
    # skip blank line after the author name
    INPUT.readline()
    
    # now read each line of the poem and store the lines in a list
    for nextLine in INPUT:
        nextLine.strip()
        if (nextLine != ""):
            allLines.append(nextLine)
            
    # close the input (original) file
    INPUT.close()        
    ReversePoem =[]
    # -----Funtion that Flips poem and reads backwords------}

    allLines.reverse()

    for lines in allLines: 
        SLines = lines.split()
        SLines.reverse()
        sentence = ' '.join(SLines) 
        sentence = sentence.lower()
        sentence = remove_punctuation(sentence)
        ReversePoem.append(sentence) 

        
    #END LOOP
    totalLines = len(ReversePoem)
    # print title and author
    OUTPUT.write("backwords poem\n")
    OUTPUT.write('Title:  {0}\n'.format( poemTitle ))
    OUTPUT.write('Author: {0}\n\n'.format( poemAuthor ))
    
    # i will start counting at the end
    i = totalLines
    
    for line in ReversePoem:
        OUTPUT.write('{0}  {1}\n'.format(i,line) )
        i = i-1
    # end of for loop
    
    OUTPUT.close()  
# end readingWordsBackwards()



#-------------------------------\
# Spell backwards read backwards \
#---------------------------------------------------------
# This fucntion maked it possible to see the spelling of the 
# backwards to catch any palindroms and to check any encryted message that 
# may lie within the poem. 
#---------------------------------------------------------
# (4)
    
    INPUT = open(poemFileName, 'r')
    
    newFileName = "Spell_Backwards_Reverse_" + poemFileName
    OUTPUT = open(newFileName, 'w')

    # make an empty list to hold all the lines of a poem
    allLines = []
    
    poemTitle  = INPUT.readline().strip()
    poemAuthor = INPUT.readline().strip()
    
    # skip blank line after the author name
    INPUT.readline()
    
    # now read each line of the poem and store the lines in a list
    for nextLine in INPUT:
        nextLine.strip()
        if (nextLine != ""):
            allLines.append(nextLine)
    
    # close the input (original) file
    INPUT.close()
    
    allLines.reverse()
    RhymeScheme = []
    # now reverse the lines in the list
    for line in allLines:
        line.split()
        line = line.lower()
        line = remove_punctuation(line)
        RhymeScheme.append(line[::-1])
        

    # get the total number of lines in this poem

    totalLines = len(RhymeScheme)
    # print title and author
    OUTPUT.write("Lines Rhyme\n")
    OUTPUT.write('Title:  {0}\n'.format( poemTitle ))
    OUTPUT.write('Author: {0}\n\n'.format( poemAuthor ))
    
    # i will start counting at the end
    i = totalLines
    
    for line in RhymeScheme:
        OUTPUT.write(line)
    # end of for loop
    
    OUTPUT.close()  


#end of Number (4)

#--------------------------------------------------------- 


#--------------------\
# remove_punctuation  \
#---------------------------------------------------------
# This function accepts a string (e.g., line of a poem)
# and removes all occurances of the default list of 
# punctuation symbols (found in Python's string.punctuation)
#---------------------------------------------------------
def remove_punctuation( s ):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
            
    return s_without_punct  
#--------------------------------------------------------- 


#-----------------------------------------------------
if __name__ == '__main__':
    main()
#-----------------------------------------------------
    
