from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
import nltk

# Notes: ex. 
#    s = " the, cinco, books, son , overdue " 
#    u = " Eng , Eng , Eng  , span,  Eng "

# for i in t : 
#     for j in nltk langs: 
#         if .... 
#          break 


# -------------------------------------------------------------

ENGLISH_STOPWORDS     = set(nltk.corpus.stopwords.words(main_language))
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


def split_count(sentence):     # split the sentence and count where each words come from 
    # how about making a parallel list and then nameing the language and word in the same index #box
    vocab_list = []
    languages_ratios = {}
    split = wordpunct_tokenize(sentence)              # tokenizes the input 
    words  = [word.lower()for word in split]          # makes sentence lower in the list split 
    lang_dict = {} 
    for language in stopwords.fileids():              # iterate through a list of lang built in 
        stopwords_set = set(stopwords.words(language)) 
        words_set = set(words)                        # creates a set of words 
        vocab_list = words                            # good
        # print "this is word set: " ,words_set
        #print "this is vocablist: " , vocab_list 
        common_element = words_set.intersection(stopwords_set)
        
        languages_ratios[language] = len(common_element) # this will detrm}ain the score
        lang_dict[language] = common_element          # works like intend, but want to make Cleaner 

        #main_language_set = 
        #secondary_lang    = lang_dict.intersection( secondary_lang) 

    # print "size of vocab: ",len(vocab_list)     #,"and lang ", len(lang_list)  ---Delete
    # for i in range(len(vocab_list)):
    #     print  lang_list[i],vocab_list[i]
    #     print "----------------------------"
    print "this is the set for main lang:", lang_dict.get(main_language), "\n"
    print "this is the set for second lang:", lang_dict.get(secondary_lang),"\n"
    # print "this lang. ratios", languages_ratios , "\n"
    # print "this is lang list: ",lang_list
    print "this is vocb_list: ", vocab_list , "\n" # check good 
    print "this is DICT: ", lang_dict
    print "ORIGINAL SENTENCE: " , sentence

    
#  -----------------  MAIN   --------------------------
# BEGINS 
#  -----------------  MAIN   --------------------------



def main(): 
    # spnish Sentence 
    
    main_language  = raw_input("what is your main language: " ) 
    secondary_lang = raw_input("what is second most used language: " ) 
    sentence_test  = raw_input("type a mix/ regular sentence: " )
    sentence_test  = sentence_test.lower()
    main_language  = main_language.lower()
    secondary_lang = secondary_lang.lower()
    



    sentence_test_spanish  = 'Hola clase como estan? Espero que esten listos la clase de hoy. I hope you all slept last night.'
    # English Sentence
    sentence_test_english = 'Hello class how are you?  I hope that you all are ready for today.  Espero que hayan dormido.'

    #French sentence 
    Sentence_test_french ="Bonjour classe"

    #swedish Sentence 
    Sentence_test_sweedish ="Hej klass" 


    simple_Sent ="Hola como estas. Espero que eses bien"
    
    # print "\n spanish"
    # ---- (count the tokens) 
    # -----------------------------------
    split_count(sentence_test)
    print "\n english"
    # split_count(sentence_test_english)
    # print "\n french"
    # split_count(Sentence_test_french)
    # print "\n sweedish"
    # split_count(Sentence_test_sweedish)
    # -----------------------------------

    # end count  of tokens 

    # PRINT  what language is the sentence 
    # PRINT  is it ENGLISH  (true or false)
    
    print "\n"
    # ------- PRINT THE SPANISH VERSION SENTENCE 
    # print get_language(sentence_test_spanish)  # Gives language 
    # print is_english(sentence_test_spanish)    # Bool is it English
    # print " -------------------\n"
    # # ------- PRINT THE FRENCH VERSION SENTENCE 
    # print get_language(Sentence_test_french)
    # print is_english(Sentence_test_french)
    # print "-------------------\n"
    # # ------- PRINT THE SWEEDISH  VERSION SENTENCE 
    # print get_language(Sentence_test_sweedish)
    # print is_english(Sentence_test_sweedish)
    # print "-------------------\n"

    # # ------- PRINT THE ENGLISH VERSION SENTENCE 
    # print get_language(sentence_test_english)   # Gives Language 
    # print is_english(sentence_test_english)     # Bool is it English 

    # Done. 
    print "\n Done. "
main() 
# End Main ()

