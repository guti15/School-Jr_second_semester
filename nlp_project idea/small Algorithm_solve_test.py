import nltk
 
ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words('english'))
NON_ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words()) - ENGLISH_STOPWORDS
 
STOPWORDS_DICT = {lang: set(nltk.corpus.stopwords.words(lang)) for lang in nltk.corpus.stopwords.fileids()}
 
def get_language(text):
    words = set(nltk.wordpunct_tokenize(text.lower()))
    return max(((lang, len(words & stopwords)) for lang, stopwords in STOPWORDS_DICT.items()), key = lambda x: x[1])[0]

def is_english(text):
    text = text.lower()
    words = set(nltk.wordpunct_tokenize(text))
    return len(words & ENGLISH_STOPWORDS) > len(words & NON_ENGLISH_STOPWORDS)


def main(): 
    sentence_test_spanish  = ' Hola calse como estan? Espero que esten listos para la clase de hoy. I hope you all slept last night.  ' 
    sentence_test_english = 'Hello class how are you?  I hope that you all are ready for today.  Espero que hayan dormido.  '

    #"Bonjour classe"  --- sweedish result  really is French
    #"Hej klass.   (sweedish) result true sweedish
    
    print get_language(sentence_test_spanish) 
    print is_english(sentence_test_spanish) 
    # ------- PRINT THE ENGLISH VERSION SENTENCE 
    print get_language(sentence_test_english) 
    print is_english(sentence_test_english) 


main() 
