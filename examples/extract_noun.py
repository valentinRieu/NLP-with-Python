import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_first_noun_phrase(text):
    # Tokenise et attribue des étiquettes morphosyntaxiques aux mots
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)

    # Définir la grammaire pour extraire les phrases nominales
    grammar = "NP: {<DT>?<JJ>*<NN.*>+<PP>*}"
    parser = RegexpParser(grammar)

    # Analyse l'arbre syntaxique et extrait les phrases nominales
    tree = parser.parse(tagged_tokens)

    # Trouve la première phrase nominale
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            np_tokens = [token for token, pos in subtree.leaves()]
            return ' '.join(np_tokens)
    return None

# Exemple d'utilisation
text = "Greenworks G40LM35K2X Tondeuse à Gazon Sans Fil pour Pelouses.."
first_noun_phrase = extract_first_noun_phrase(text)
print(f"Première phrase nominale: {first_noun_phrase}")
