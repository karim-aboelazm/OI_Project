import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer 
stemmer = PorterStemmer()

def tokenize(txt): 
    return nltk.word_tokenize(txt)

def stem(word): 
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_txt,words):
    stem_word = [stem(word) for word in tokenized_txt]
    bag = np.zeros(len(words),dtype=np.float32)

    for indx , w in enumerate(words): 
        if w in stem_word:
            bag[indx] = 1
    return bag