import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, ne_chunk

text = "The university Jean Monnet is a French institution headquartered in Saint-Etienne, Auvergne-Rhone-Alpes." \
        " It forms students for a master degree and a Ph.D in a variety of cursus."

# Tokenization et étiquetage grammatical
sentences = sent_tokenize(text)
for sent in sentences:
    tokens = word_tokenize(sent)
    tagged_tokens = pos_tag(tokens)

    # Reconnaissance d'entités nommées
    named_entities = ne_chunk(tagged_tokens)
    print(named_entities)
