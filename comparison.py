from summa import keywords
from typing import Union
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def most_associate_topic(word_dump: str, topics: list) -> Union[str, None]:
    keywords_list = keywords.keywords(word_dump, ratio=.9).split()
    # keywords_synonyms = []
    # for keyword in keywords_list:
    #     for syn in wordnet.synsets(keyword):
    #         for l in syn.lemmas():
    #             keywords_synonyms.append(l.name())
    # topics_synonyms = []
    # for topic in topics:
    #     for syn in wordnet.synsets(topic):
    #         for l in syn.lemmas():
    #             topics_synonyms.append(l.name())

    return intersection(keywords_list, topics)