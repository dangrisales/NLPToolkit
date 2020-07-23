#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:13:14 2020

@author: daniel
"""
import string
import spacy
from nltk.corpus import stopwords
import unicodedata
from nltk.stem.porter import PorterStemmer
from nltk import wordpunct_tokenize
import re

#%% noPunctuation
def noPunctuation(text):
    

    
    
    text= [char for char in text if char not in string.punctuation]
    nopunctuation=''.join(text)
    
    
    
    
    nopunctuation.split()
    #nopunctuation= [word for word in wordpunct_tokenize(text)]


    """ print('1',nopunctuation)
    nopunctuation=''.join(nopunctuation)
    print('2',nopunctuation)

    print('3',nopunctuation)

    #Now eliminate the punctuation and convert into a whole sentence
    #nopunctuation=''.join(nopunctuation)

    #Split each words present in the new sentence
    nopunctuation.split()
    print('4',nopunctuation)"""
    #nopunctuation= [word for word in wordpunct_tokenize(nopunctuation)]

    return nopunctuation
#%%

def noPunctutionExtra(text):
    
    texttoP=text
    forbidden1 = ('?', '¿', '¡', '!', ',', '.', ';', ':')
    for i in range (len(forbidden1)):
    
        idx=[n for n in range(len(texttoP)) if text.find(forbidden1[i], n) == n]
        if len(idx)!=0:
            for j in range(len(idx)):
                texttoP=texttoP.replace(texttoP[idx[j]],' ')
    #print(text)
    return texttoP


 #%%   
def removeURL(text):
    idx1=[n for n in range(len(text)) if text.find('((', n) == n]
    idx2=[n for n in range(len(text)) if text.find('))', n) == n]
    idxlen=len(idx1)
    idxlen2=len(idx2)
    segurity_count=0
    segurity_flag=True
    
    while idxlen!=0 and segurity_flag:
        
            
        segurity_count+=1    
        if len(idx1)!=0 and len(idx2)!=0:
            if idx1[0]<idx2[0]:
                    text=text.replace(text[idx1[0]:idx2[0]+1],"")
                    
            else:
                    text=text.replace(text[idx1[0]:idx2[1]+1],"")
        elif len(idx1)!=0:

            text=text.replace(text[idx1[0]:len(text)],"")
        #maximo 50 links por interaccion    
        if segurity_count>50:
            print('¡ERROR! problemas para preprocesar el texto: ',text)
            segurity_flag = False
        
        
    
        idx1=[n for n in range(len(text)) if text.find('((', n) == n]
        idx2=[n for n in range(len(text)) if text.find('))', n) == n]
        idxlen=len(idx1)
        #print(idxlen)
        idxlen2=len(idx2)
        #print(idx1)


    #print(text)

    return text

#%%
def removeNumbers(text):
    text = ''.join([i for i in text if not i.isdigit()])
    
    return text
#%%
def removeEmojis(text):
    
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text) # no emoji
#%% StopWordsRemoval
def StopWordsRemoval(text,language='spanish'):
    #Now eliminate stopwords
    clean_sentence= [word for word in text.split() if word.lower() not in stopwords.words('spanish')]
    clean_sentence=' '.join(clean_sentence)

    return clean_sentence

#%% Lemmatizer
def Lemmatizer(text,language='spanish'):
    #nlp = en_core_web_sm.load()
    nlp = spacy.load('es_core_news_sm')
    #nlp = spacy.load('es_core_news_md')
    doc = nlp(text)
    tokenLemma=[]

    for token in doc:
        #print(token, token.lemma, token.lemma_)
        tokenLemma.append(token.lemma_)
    tokenLemma=' '.join(tokenLemma)
    return tokenLemma


#%% Lemmatizer
def stemming(text,language='spanish'):
    
    #First Tokenaize
    words = [word for word in wordpunct_tokenize(text)]

    
    #Stemming
    porter_stemmer = PorterStemmer()
    stemmers = [porter_stemmer.stem(word) for word in words]
    textStemm = [stem for stem in stemmers if stem.isalpha() and len(stem) > 1]
    
    textStemm=' '.join(textStemm)

    
    return textStemm


#%%
def botonSel(text):
    idx1=[n for n in range(len(text)) if text.find('botones seleccion:', n) == n]
    idx2=[n for n in range(len(text)) if text.find('))', n) == n]
    idxlen=len(idx1)
    idxlen2=len(idx2)
    
    
    while idxlen!=0:
        
        if idx1[0]<idx2[0]:
                text=text.replace(text[idx1[0]:idx2[0]+1],"")
                
        else:
                text=text.replace(text[idx1[0]:idx2[1]+1],"")
                
        
        
    
        idx1=[n for n in range(len(text)) if text.find('boton enlace:', n) == n]
        idx2=[n for n in range(len(text)) if text.find('))', n) == n]
        idxlen=len(idx1)
        #print(idxlen)
        idxlen2=len(idx2)
        #print(idx1)


    #print(text)
    return text
        
        
#%% HesitationsRemoval

def HesitationsRemoval(text):

    idx1=[n for n in range(len(text)) if text.find('[', n) == n]
    idx2=[n for n in range(len(text)) if text.find(']', n) == n]
    idxlen=len(idx1)
    idxlen2=len(idx2)
 

    while idxlen>0 and idxlen2:
        
        
        
        text=text.replace(text[idx1[0]:idx2[0]+1],"")
        

        idx1=[n for n in range(len(text)) if text.find('[', n) == n]
        idx2=[n for n in range(len(text)) if text.find(']', n) == n]
        idxlen=len(idx1)
        idxlen2=len(idx2)
        
        #print(idx1)


    #print(text)
    return text


#%% spk1Removal

def spk1Removal(text):



    text=text.replace('spk1',"")
    text=text.replace(' AH '," ")
    text=text.replace(' EH '," ")

    return text
#%% toLowerCase

def toLowerCase(text):
    text=text.lower()
    return text

#%% accentRemoval
    

def accentRemoval(df):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    data = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', df).translate(trans_tab))

    return data


def preprocess(texto):
    text = toLowerCase(texto)

    text = removeEmojis(text)

    text = removeURL(text)


    text = botonSel(text)

    text = noPunctuation(text)

    
    text = removeNumbers(text)

    text = noPunctuation(text)


    text = noPunctutionExtra(text)


    text = accentRemoval(text)

    

    return ProcessingText_AR


