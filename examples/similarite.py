import nltk
from nltk.corpus import wordnet

# Calcule la similarité entre deux listes de synonymes
def similarite(synsets1, synsets2):
    max_similarity = 0
    for synset1 in synsets1:
        for synset2 in synsets2:
            similarity = synset1.path_similarity(synset2)
            if similarity is not None and similarity > max_similarity:
                max_similarity = similarity
    return max_similarity


text1 = 'The small dog'.split(" ")
text2 = 'The little hound'.split(" ")


# Trouve les synonymes pour chaque mot
similarite_totale = 0
for word1, word2 in zip(text1, text2):
    synset_word1 = wordnet.synsets(word1)
    synset_word2 = wordnet.synsets(word2)

    similarite_totale += similarite(synset_word1, synset_word2)

print(f"Similarité entre ces deux phrases : {similarite_totale}")
