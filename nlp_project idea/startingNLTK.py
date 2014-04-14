# recognize a language and then see what languge is it mostly heavliy # on.  ---> possibly bank out words in a diffrent language and then # #define them towards the end 
# make progresss. on this and show our work on the progress
# Practice For NlTK 
# (feels like a fail)  

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords



def main(): 
#step 1 which tokenizes the words and now we have clean words to stop match against stop 

    print "\n -----------------------------\n"
    split = wordpunct_tokenize("hola como estas, espero que estes bien" )
    print split
    print "\n -----------------------------\n"
    #
    #Lets Get serious 
    #
    languages_ratios = {}
    tokens = wordpunct_tokenize("hola como estas?")
    words = [word.lower() for word in tokens]
    for language in stopwords.fileids(): 
        stopwords_set = set(stopwords.words(language))
        words_set = set(words) 
        common_element = words_set.intersection(stopwords_set)
        languages_ratios[language] = len(common_element) # this will detrmain the score

    print languages_ratios


main()

#   Brief summary  --- Manage ( to grab all the stop words and base the primar languge of that ) 
#  - so what I have done:: I have tokenized the Word
#  - made the words into lower case then placed them in a list
#  - made a for loop to to read in each word and then
#  - 
#  -  
