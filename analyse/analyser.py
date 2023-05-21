import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.classify import accuracy


def create_word_features(words):
    my_dict = dict([(word, True) for word in words])
    return my_dict


def tokenize(s: str):
    return word_tokenize(s.lower())

def applyTheoricalNote(comment):
    return int(classifier.classify(create_word_features(comment)))

train = pd.read_csv("train.csv")  # Chargement des données d'entrainement
test = pd.read_csv("test.csv")  # Chargement des données de test

train['tokenized'] = train['Commentaire'].apply(tokenize)
test['tokenized'] = test['Commentaire'].apply(tokenize)

data = []
test_set = []

for i in range(len(train)):
    data += [(create_word_features(train['tokenized'][i]), train['NoteC'][i])]

for i in range(len(test)):
    test_set += [(create_word_features(test['tokenized'][i]), test['NoteC'][i])]

classifier = nltk.NaiveBayesClassifier.train(data)



test["TheoricalNote"] = test["tokenized"].apply(applyTheoricalNote)

test["Error"] = test["TheoricalNote"] - test["NoteC"]

total = 0
maxError = 0
minError = 5
MagnifyingError = 0
EmpiricalError = 0
for i in range(len(test)):
    if test["Error"][i] == 0:
        total += 1
    if abs(test["Error"][i]) > maxError:
        maxError = abs(test["Error"][i])
    if abs(test["Error"][i]) < minError and abs(test["Error"][i]) != 0:
        minError = abs(test["Error"][i])
    if test["Error"][i] > 0:
        EmpiricalError += 1
    if test["Error"][i] < 0:
        MagnifyingError += 1

print("Précision: " + str(total/len(test)*100) + "%" )
print("Erreur max: " + str(maxError))
print("Erreur min: " + str(minError))
print("Erreur réductrice: " + str(EmpiricalError/(len(test)-total)*100) + "%")
print("Erreur amplificatrice: " + str(MagnifyingError/(len(test)-total)*100) + "%")

print(classifier.classify(create_word_features(tokenize(str(input("Entrez un commentaire: "))))))
