from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
import nltk
 
ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words('english'))
NON_ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words()) - ENGLISH_STOPWORDS
 
STOPWORDS_DICT = {lang: set(nltk.corpus.stopwords.words(lang)) for lang in nltk.corpus.stopwords.fileids()}
 

def get_language(text):    # tell me the Languge 
    words = set(nltk.wordpunct_tokenize(text.lower()))
    return max(((lang, len(words & stopwords)) for lang, stopwords in STOPWORDS_DICT.items()), key = lambda x: x[1])[0]
# end fuction 


def is_english(text):     #is it an English Sentence
    text = text.lower()
    words = set(nltk.wordpunct_tokenize(text))
    return len(words & ENGLISH_STOPWORDS) > len(words & NON_ENGLISH_STOPWORDS)
#end fuction 


def split_count(sentence):     # slit the sentence and count where each words come from 
    languages_ratios = {}
    split = wordpunct_tokenize(sentence)  # tokenizes the input 
    words  = [word.lower()for word in split]  # makes sentence lower in the list split 

    for language in stopwords.fileids(): 
        stopwords_set = set(stopwords.words(language))  #creats a set of language based on the token lang.

        words_set = set(words)  # creates a set of words 
        common_element = words_set.intersection(stopwords_set)
        languages_ratios[language] = len(common_element) # this will detrmain the score
    print languages_ratios
        


#  -----------------  MAIN   --------------------------

def main(): 
    # spnish Sentence 
    sentence_test_spanish  = ' Hola calse como estan? Espero que esten listos para la clase de hoy. I hope you all slept last night.  ' 
    # English Sentence
    sentence_test_english = 'Hello class how are you?  I hope that you all are ready for today.  Espero que hayan dormido.  '

    #French sentence 
    Sentence_test_french ="Bonjour classe"

    #swedish Sentence 
    Sentence_test_sweedish ="Hej klass" 


    simple_Sent ="Hola como estas. Espero que eses bien"
    
    print "\n spanish"
    # ---- (count the tokens) 
    split_count(sentence_test_spanish)
    print "\n english"
    split_count(sentence_test_english)
    print "\n french"
    split_count(Sentence_test_french)
    print "\n sweedish"
    split_count(Sentence_test_sweedish)
    # end count  of tokens 

    # PRINT  what language is the sentence 
    # PRINT  is it ENGLISH  (true or false)
    
    print "\n"
    # ------- PRINT THE SPANISH VERSION SENTENCE 
    print get_language(sentence_test_spanish)  # Gives language 
    print is_english(sentence_test_spanish)    # Bool is it English
    print " -------------------\n"
    # ------- PRINT THE FRENCH VERSION SENTENCE 
    print get_language(Sentence_test_french)
    print is_english(Sentence_test_french)
    print "-------------------\n"
    # ------- PRINT THE SWEEDISH  VERSION SENTENCE 
    print get_language(Sentence_test_sweedish)
    print is_english(Sentence_test_sweedish)
    print "-------------------\n"

    # ------- PRINT THE ENGLISH VERSION SENTENCE 
    print get_language(sentence_test_english)   # Gives Language 
    print is_english(sentence_test_english)     # Bool is it English 

    # Done. 
    print "\n Done. "
main() 
