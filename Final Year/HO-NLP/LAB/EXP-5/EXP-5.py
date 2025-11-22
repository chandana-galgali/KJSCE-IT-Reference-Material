import collections

corpus = [
    "A boy is playing in the park",
    "A girl is playing with a dog",
    "The dog is running in the park",
    "The boy is running after the dog"
]

sentence_to_calculate = "The boy is playing with a dog"

print("--- Preprocessing Data ---")
tokenized_corpus = [['<s>'] + s.lower().split() + ['</s>'] for s in corpus]
tokenized_sentence = ['<s>'] + sentence_to_calculate.lower().split() + ['</s>']
print("Tokenized Target Sentence:", tokenized_sentence)
print("-" * 25)

print("--- Counting Frequencies from Corpus ---")
all_words = [word for sent in tokenized_corpus for word in sent]
unigram_counts = collections.Counter(all_words)
bigram_counts = collections.Counter()
for sent in tokenized_corpus:
    bigram_counts.update(zip(sent, sent[1:]))

print(f"Unigram Count for 'boy': {unigram_counts['boy']}")
print(f"Bi-gram Count for ('is', 'playing'): {bigram_counts[('is', 'playing')]}")
print("-" * 25)

print(f"--- Calculating Probability for: '{sentence_to_calculate}' ---")
sentence_probability = 1.0
sentence_bigrams = list(zip(tokenized_sentence, tokenized_sentence[1:]))

for bigram in sentence_bigrams:
    prev_word, current_word = bigram
    bi_count = bigram_counts[bigram]
    uni_count = unigram_counts[prev_word]
    
    if uni_count == 0 or bi_count == 0:
        conditional_prob = 0
    else:
        conditional_prob = bi_count / uni_count
        
    print(f"P({current_word:^9} | {prev_word:^9}) = {bi_count} / {uni_count} = {conditional_prob:.4f}")
    sentence_probability *= conditional_prob

print("-" * 25)
print("--- Final Result ---")
print(f"The probability of the sentence is: {sentence_probability}")
print(f"P('{sentence_to_calculate}') = {sentence_probability:.6f}")