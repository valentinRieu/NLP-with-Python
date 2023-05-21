import nltk
from nltk.corpus import reuters
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from random import shuffle

# Fonction pour extraire des caractéristiques d'un document
def document_features(document):
    tokens = set(nltk.word_tokenize(document.lower()))
    features = {}
    for word in tokens:
        features[f'contains({word})'] = True
    return features


# Catégories présentes dans le corpus Reuters
categories = ['crude', 'money-fx', 'coffee', 'corn', 'earn']

# categories.append('fuel') => réduit la précision
train_data = []
test_data = []

# création d'un set de test et training différenciés pour chaque catégorie
for category in categories:
    for fileid in reuters.fileids(category):
        document = ' '.join(reuters.words(fileid))
        features = document_features(document)
        label = category
        if fileid.startswith('training'):
            train_data.append((features, label))
        else:
            test_data.append((features, label))


shuffle(train_data)
shuffle(test_data)

# Entrainement sur le set de training
classifier = NaiveBayesClassifier.train(train_data)

# Calcul précision du modèle entraîné (outil NLTK)
print(f"Précision du classificateur: {accuracy(classifier, test_data):.2f}")

# On classe maintenant
sample_text = "Oil prices increased significantly due to geopolitical tensions in the Middle East."
sample_features = document_features(sample_text)
predicted_label = classifier.classify(sample_features)
print(f"Texte: {sample_text}")
print(f"Catégorie prédite: {predicted_label}")
