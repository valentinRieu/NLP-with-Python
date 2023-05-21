import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet

lemmatiseur = WordNetLemmatizer()
stemmer = PorterStemmer()


def wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'): return wordnet.ADJ
    if treebank_tag.startswith('V'): return wordnet.VERB
    if treebank_tag.startswith('N'): return wordnet.NOUN
    if treebank_tag.startswith('R'): return wordnet.ADV
    return ''


def analyse_morphologique(mot, tag):
    lemme = lemmatiseur.lemmatize(mot, pos=tag)
    racine = stemmer.stem(mot)
    return {"mot": mot, "lemme": lemme, "racine": racine}


text = "don't father's parents' birds flies knives being flying lovely axes glasses given greatest faster lovelier " \
       "mashed bathed accessed"
tokens = text.split(" ")
tagged = nltk.pos_tag(tokens)
for token, tag in tagged:
    print(analyse_morphologique(token, wordnet_pos(tag)))