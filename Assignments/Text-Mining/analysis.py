from Tokenization import *
import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def create_text(hist):
    '''
    Convering dict to str on word frequencies.
    Keys = str words
    Value = Int word freq
    '''

    result = str()
    for i in hist:
        for j in range(hist[i]):
            result = result + ' ' + i
    return result

def cosine_sim()