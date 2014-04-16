from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
import nltk
 
ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words('english'))
NON_ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words()) - ENGLISH_STOPWORDS
 
STOPWORDS_DICT = {lang: set(nltk.corpus.stopwords.words(lang)) for lang in nltk.corpus.stopwords.fileids()}
 


# tell me the Languge 
def get_language(text):
    words = set(nltk.wordpunct_tokenize(text.lower()))
    return max(((lang, len(words & stopwords)) for lang, stopwords in STOPWORDS_DICT.items()), key = lambda x: x[1])[0]

#is it an English Sentence
def is_english(text):
    text = text.lower()
    words = set(nltk.wordpunct_tokenize(text))
    return len(words & ENGLISH_STOPWORDS) > len(words & NON_ENGLISH_STOPWORDS)

def split_count(sentence): 
    languages_ratios = {}
    split = wordpunct_tokenize(sentence)
    words  = [word.lower()for word in split]
    for language in stopwords.fileids(): 
        stopwords_set = set(stopwords.words(language))
        words_set = set(words) 
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
    
    print "\n"

    split_count(sentence_test_spanish)
    

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
