#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Subcode is used to split query content and extract nouns



import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string






def query_noun(document):
    lowers = document.lower()
    #remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    lemmatizer = WordNetLemmatizer()
    tokens_lemma =  [lemmatizer.lemmatize(t) for t in tokens]
    tokens_lemma_one = list(set(tokens_lemma))      # list去重    
    stop_words = stopwords.words('english')
    query_lexical = [w for w in tokens_lemma_one if w not in stop_words]
    lexical_pos = nltk.pos_tag(query_lexical)
    query = [word for (word, tag) in lexical_pos if tag.startswith('N')]          # extract nouns
    query_keywords = ' '.join(query)
    return query_keywords



if __name__ == "__main__":
    document = open('D:/knowledge_network/paper_3/design_problem.txt', encoding='utf8').read()
    query = query_noun(document)
    print(query)