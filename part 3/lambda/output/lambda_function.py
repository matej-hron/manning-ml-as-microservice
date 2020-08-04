import json
import regex
import nltk
from nltk import download
from nltk.corpus import stopwords
from string import punctuation
import pickle
import sys
from nltk.tokenize import word_tokenize


def extract_features(words, stopwords_eng):
    return [w for w in words if w not in stopwords_eng and w not in punctuation]


def bag_of_words(words):
    bag = {}
    for w in words:
        bag[w] = bag.get(w, 0)+1
    return bag


def get_sentiment(review, stopwords_eng, model):
    words = word_tokenize(review)
    words = extract_features(words, stopwords_eng)
    words = bag_of_words(words)
    return model.classify(words)


def lambda_handler(event, context):
    nltk.data.path.append("/tmp")
    download('punkt', download_dir="/tmp")
    download('stopwords', download_dir="/tmp")
    stopwords_eng = stopwords.words('english')

    model_file = open('sa_classifier2.pickle', 'rb')
    model = pickle.load(model_file)
    model_file.close()

    sentiment = get_sentiment(event['review'], stopwords_eng, model)

    return {
        'statusCode': 200,
        'body': json.dumps(sentiment)
    }
