import nltk
import random
from nltk.corpus import inaugural
from nltk.tokenize import sent_tokenize, word_tokenize


# Modèle de machine learning basique
class Model:
    def __init__(self, n):
        self.n = n
        self.model = {}

    def train(self, tokens):
        for ngram in nltk.ngrams(tokens, self.n):
            prefix, word = tuple(ngram[:-1]), ngram[-1]
            if prefix not in self.model:
                self.model[prefix] = []
            self.model[prefix].append(word)

    def generate(self, prefix, num_words):
        generated_tokens = list(prefix)
        for _ in range(num_words):
            prefix_tuple = tuple(generated_tokens[-(self.n - 1):])
            if prefix_tuple in self.model:
                next_word = random.choice(self.model[prefix_tuple])
                generated_tokens.append(next_word)
            else:
                # Recherche d'un préfixe alternatif pour continuer la génération
                alt_prefix = random.choice(list(self.model.keys()))
                generated_tokens.extend(alt_prefix)
        generated_tokens.extend("(...)")
        return ' '.join(generated_tokens)

n = 3
model = Model(n)

# On entraine le modèle avec des articles de Inaugural (discours de présidents des É-U)
tokens = []
for fileid in inaugural.fileids()[50:]:
    sentences = sent_tokenize(inaugural.raw(fileid))
    for sentence in sentences:
        tokens.extend(word_tokenize(sentence))
model.train(tokens)

# Génère une séquence de texte
generated_text = model.generate(["The", "American", "Revolutionary", "war"], 50)
print(generated_text)
