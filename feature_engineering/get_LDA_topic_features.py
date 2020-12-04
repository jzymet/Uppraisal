import pandas as pd
import numpy as np
import requests
import json
import csv
import re
import string
import os
import spacy
import warnings
from pandas import DataFrame
from gensim.models import Phrases
from gensim.corpora import Dictionary
from gensim.models import LdaModel

def LDA(laptopData: DataFrame) -> DataFrame:

    # delete special characters, but without using re.sub(r'[^a-zA-Z\s]', '', t), to avoid losing emojis
    laptopData['description'] = [re.sub(r'(!|"|#|\$|%|&|\'|\(|\)|\*|\+|,|-|\.|/|:|;|<|=|>|\?|@|\[|\\|\]|\^|_|`|{|\||}|~)+', ' ', str(t)) for t in laptopData['description']]
    # replace any double spaces with single
    laptopData['description'] = [re.sub(r'\s+\s', ' ', str(t)).strip() for t in laptopData['description']]

    #tokenize our texts spaCy's en_core_web_sm model
    nlp = spacy.load('en_core_web_sm')
    texts = laptopData['description'].tolist()
    spacy_docs = list(nlp.pipe(texts))

    #lemmatize and lowercase tokens, drop stop words, exclude lemmata that are too short or long
    docs = [[t.lemma_.lower() for t in doc if len(t.orth_) > 3 and len(t.orth_) < 15 and not t.is_stop] for doc in spacy_docs]

    #print preprocessing results
    for i in range(5):
        print(docs[i])
        print('\n')

    #take frequent bigrams into account
    bigram = Phrases(docs, min_count=10)
    tokens = []
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                docs[idx].append(token)
                tokens.append(token)

    #print bigrams
    print(list(set(tokens))[:10])

    #more preprocessing!: create a dictionary representation of the documents to create (wordID, freq)-pairs of each document
    dictionary = Dictionary(docs)
    print('Number of unique words in original documents:', len(dictionary))

    #remove the least and most frequent words from the vocabulary
    dictionary.filter_extremes(no_below=3, no_above=0.25)
    print('Number of unique words after removing rare and common words:', len(dictionary))

    #example representation
    print("Example representation of document 3:", dictionary.doc2bow(docs[2]))

    #create bag-of-words representations from (wordID, freq)-pairs
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    # train LDA model
    model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=8, chunksize=500, passes=3, random_state=1)

    # LDA model results
    for (topic, words) in model.print_topics():
        print(topic + 1, ":", words, '\n')

    #some topics recognized in individual texts
    for (text, doc) in zip(texts[:20], docs[:20]):
        print(text)
        print('-'*10)
        print([(topic+1, prob) for (topic, prob) in model[dictionary.doc2bow(doc)]])
        print('\n')

    #looping through all texts, let's save most likely topic number
    topic_nums = []

    for (text, doc) in zip(texts, docs):
        probs = np.array(model[dictionary.doc2bow(doc)])
        topic_nums.append(probs)
    print(texts[0])
    print(topic_nums[0])

    #(write csv for my own exploration)
    f = csv.writer(open("topicValues.csv", "w"))
    f.writerow(["0", "1", "2", "3", "4", "5", "6", "7",])
    for desc in topic_nums:
        d1 = [0, 0, 0, 0, 0, 0, 0, 0]
        for x in desc.tolist():
            if x[0] == 0.0:
                d1[0] = x[1]
            elif x[0] == 1.0:
                d1[1] = x[1]
            elif x[0] == 2.0:
                d1[2] = x[1]
            elif x[0] == 3.0:
                d1[3] = x[1]
            elif x[0] == 4.0:
                d1[0] = x[1]
            elif x[0] == 5.0:
                d1[5] = x[1]
            elif x[0] == 6.0:
                d1[6] = x[1]
            elif x[0] == 7.0:
                d1[7] = x[1]
        f.writerow([d1[0], d1[1], d1[2], d1[3], d1[4], d1[5], d1[6], d1[7]])

    #return dataFrame quantifying for each topic T the degree to which each description belongs to T
    return pd.read_csv("topicValues.csv", encoding = 'ISO-8859-1')