import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')

text_corpus = """
Natural language processing (NLP) is a subfield of linguistics, computer science,
and artificial intelligence concerned with the interactions between computers and human language.
It is an extremely interesting field that has been growing rapidly in recent years.
NLP technologies are being used for various applications, including chatbots, machine
translation, and sentiment analysis. The challenges in NLP are many, but researchers are
making great progress. Understanding context, dealing with ambiguity, and handling different
languages are some of the key problems. These challenges are being tackled by using advanced
machine learning models, especially deep learning.
"""

words = word_tokenize(text_corpus.lower())

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

lemmatizer = WordNetLemmatizer()

lemmatized_words_no_pos = [lemmatizer.lemmatize(word) for word in filtered_words]

print("--- Lemmatization without POS Tagging ---")
print("Original words:", filtered_words[:15]) 
print("Lemmatized words:", lemmatized_words_no_pos[:15])
print("-" * 50)

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  

pos_tagged_words = pos_tag(filtered_words)

lemmatized_words_pos = []
for word, tag in pos_tagged_words:
    wntag = get_wordnet_pos(tag)
    lemmatized_words_pos.append(lemmatizer.lemmatize(word, pos=wntag))

print("--- Lemmatization with POS Tagging ---")
print("Original words:", filtered_words[:15])
print("Lemmatized words (with POS):", lemmatized_words_pos[:15])
print("-" * 50)