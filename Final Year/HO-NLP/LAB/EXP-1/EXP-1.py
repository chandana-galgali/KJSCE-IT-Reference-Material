import re
import nltk
from textblob import TextBlob
from gensim.utils import simple_preprocess
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.tokenize import (
    word_tokenize, sent_tokenize, RegexpTokenizer,
    TreebankWordTokenizer, TweetTokenizer, MWETokenizer
)
import spacy
import en_core_web_sm

# =======================
# Setup
# =======================
nltk.download('punkt', quiet=True)
nlp = en_core_web_sm.load()

# =======================
# Sample Texts
# =======================
texts = {
    "Tweet": """OMG 😱 New phone drop!!! Check this out: https://t.co/abcd
@realUser can’t wait 😂🔥 #TechNews #NewLaunch""",
    "News": (
        "The Reserve Bank raised interest rates by 25 basis points on Tuesday, "
        "citing persistent inflation. Analysts expect a cautious outlook through Q4 2025."
    ),
    "General": (
        "But I'm glad you'll see me as I am. Above all, I wouldn't want people to think "
        "that I want to prove anything. I just want to live; to cause no evil to anyone "
        "but myself. I have that right, haven't I? — Leo Tolstoy"
    )
}

# =======================
# 1) Python split & regex
# =======================
def py_split_tokens(text):
    return text.split()

def regex_word_tokens(text, pattern=r"\w+"):
    return re.findall(pattern, text)

regex_social = r"(https?://\S+)|(@\w+)|(#\w+)|(\w+’\w+)|(\w+'\w+)|(\w+)"
def regex_social_tokens(text):
    raw = re.findall(regex_social, text)
    return [next(g for g in m if g) for m in raw]

# =======================
# 2) NLTK tokenizers
# =======================
tb = TreebankWordTokenizer()
tt = TweetTokenizer(strip_handles=False, reduce_len=True, preserve_case=False)
regexp_tokenizer = RegexpTokenizer(r"\w+")
mwe = MWETokenizer([("New", "York"), ("machine", "learning"), ("interest", "rates")], separator="_")

def mwe_tokens(text):
    return mwe.tokenize(word_tokenize(text))

# =======================
# 3) TextBlob
# =======================
def textblob_tokens(text):
    blob = TextBlob(text)
    return [str(s) for s in blob.sentences], blob.words

# =======================
# 4) spaCy
# =======================
def spacy_tokens(text):
    doc = nlp(text)
    return [t.text for t in doc]

def spacy_sentences(text):
    doc = nlp(text)
    return [s.text for s in doc.sents]

# =======================
# 5) Gensim
# =======================
def gensim_tokens(text):
    return simple_preprocess(text)

# =======================
# 6) Keras
# =======================
def keras_tokens(text):
    return text_to_word_sequence(text)

# =======================
# 7) RegexpTokenizer Examples
# =======================
def regexp_examples():
    text = "The price of the car is 50,000 dollars. Model-X isn't cheap!"
    print("\nRegexpTokenizer (\\w+):", RegexpTokenizer(r"\w+").tokenize(text))
    print("RegexpTokenizer (keep apostrophes):",
          RegexpTokenizer(r"[A-Za-z]+(?:'[A-Za-z]+)?").tokenize(text))
    print("RegexpTokenizer (numbers with commas/decimals):",
          RegexpTokenizer(r"\d[\d,\.]*").tokenize(text))

# =======================
# 8) Observations
# =======================
def observe(name, txt):
    wb = word_tokenize(txt)
    tw = TweetTokenizer(preserve_case=False).tokenize(txt)
    sp = [t.text for t in nlp(txt)]
    gs = simple_preprocess(txt)
    kz = text_to_word_sequence(txt)

    print(f"\n=== Observations: {name} ===")
    print("NLTK word_tokenize:", wb[:10])
    print("TweetTokenizer:", tw[:10])
    print("spaCy:", sp[:10])
    print("Gensim:", gs[:10])
    print("Keras:", kz[:10])

# =======================
# Main execution
# =======================
if __name__ == "__main__":
    for name, txt in texts.items():
        print(f"\n==== {name} ====")
        print("--- Python split:", py_split_tokens(txt))
        print("--- Regex \\w+:", regex_word_tokens(txt))
        print("--- Regex social-aware:", regex_social_tokens(txt))

        print("\nNLTK:")
        print("Sentence:", sent_tokenize(txt))
        print("Word:", word_tokenize(txt))
        print("Treebank:", tb.tokenize(txt))
        print("Tweet:", tt.tokenize(txt))
        print("Regexp:", regexp_tokenizer.tokenize(txt))
        print("MWE:", mwe_tokens(txt))

        print("\nTextBlob:")
        sents, words = textblob_tokens(txt)
        print("Sentences:", sents)
        print("Words:", words)

        print("\nspaCy:")
        print("Sentences:", spacy_sentences(txt))
        print("Tokens:", spacy_tokens(txt))

        print("\nGensim:", gensim_tokens(txt))
        print("Keras:", keras_tokens(txt))

        observe(name, txt)

    regexp_examples()