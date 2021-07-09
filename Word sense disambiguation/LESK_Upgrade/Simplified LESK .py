#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class SimplifiedLesk: 
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))

    def disambiguate(self, word, sentence):       
        word_senses = wordnet.synsets(word)
        best_sense = word_senses[0]  # Assume that first sense is most freq.
        max_overlap = 0
        context = set(word_tokenize(sentence))
        for sense in word_senses:
            signature = self.tokenized_gloss(sense)
            overlap = self.compute_overlap(signature, context)            
            if overlap > max_overlap:
                max_overlap = overlap
                best_sense = sense
        return best_sense  
    
    
    def tokenized_gloss(self, sense):        
        tokens = set(word_tokenize(sense.definition()))
        for example in sense.examples():
            tokens.union(set(word_tokenize(example)))
        return tokens

    def compute_overlap(self, signature, context):       
        sig = signature.difference(self.stopwords)
        return len(sig.intersection(context))


# In[2]:


model=SimplifiedLesk()
model.disambiguate('knife', 'She chopped the vegetables with a chef’s knife.')

