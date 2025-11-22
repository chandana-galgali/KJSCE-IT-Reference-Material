import collections

# --- Grammar Definition ---
# The grammar is defined as a dictionary where keys are the non-terminals
# and values are lists of possible right-hand side productions (RHS).
GRAMMAR = {
    'S': ['NP VP'],          # Sentence -> Noun Phrase Verb Phrase
    'NP': ['Det N', 'N'],    # Noun Phrase -> Determiner Noun | Noun
    'VP': ['V NP', 'V'],     # Verb Phrase -> Verb Noun Phrase | Verb
    'Det': ['the', 'a'],     # Determiner -> 'the' | 'a'
    'N': ['cat', 'dog', 'park'],  # Noun -> 'cat' | 'dog' | 'park'
    'V': ['chased', 'ran', 'saw'] # Verb -> 'chased' | 'ran' | 'saw'
}

# --- Parsing Function (CYK-like Bottom-Up Parsing) ---

def parse_sentence(sentence, grammar):
    """
    Implements a basic bottom-up parsing technique (simplified CYK)
    to check if a sentence can be derived from the grammar.
    """
    words = sentence.lower().split()
    n = len(words)

    if n == 0:
        return []

    # Initialize the parsing table (a list of dictionaries)
    # table[i][j] will store the set of non-terminals that span words[i...j]
    table = collections.defaultdict(lambda: collections.defaultdict(set))

    # 1. Initialization (Filling in the diagonal for single words)
    print("--- Step 1: Matching Terminals (Words) ---")
    for i in range(n):
        word = words[i]
        found_non_terminals = set()
        for non_term, productions in grammar.items():
            # Check if the word matches any single-terminal production (POS tag)
            if [word] in productions:
                found_non_terminals.add(non_term)
        table[i][i] = found_non_terminals
        print(f"Cell[{i},{i}] for '{word}': {list(found_non_terminals)}")
    
    print("\n--- Step 2: Combining Sub-phrases (Bottom-Up Reduction) ---")
    # 2. Iteration (Combining sub-phrases)
    for length in range(2, n + 1):  # length of span
        for i in range(n - length + 1):  # start index
            j = i + length - 1  # end index
            
            # K is the split point: words[i...k] and words[k+1...j]
            for k in range(i, j): 
                # Sub-phrases are spanned by non-terminals X and Y
                B_set = table[i][k]   # Non-terminals spanning words[i...k]
                C_set = table[k+1][j] # Non-terminals spanning words[k+1...j]
                
                # Check all combinations of B and C
                for B in B_set:
                    for C in C_set:
                        two_symbol_rhs = f"{B} {C}"
                        # Check if any non-terminal 'A' in the grammar can produce 'B C'
                        for A, productions in grammar.items():
                            if two_symbol_rhs in productions:
                                table[i][j].add(A)
                
            print(f"Cell[{i},{j}] (Span '{' '.join(words[i:j+1])}'): {list(table[i][j])}")

    # 3. Final Result (Check the top-right cell for the Start Symbol 'S')
    start_symbol = 'S'
    if start_symbol in table[0][n-1]:
        print(f"\n✅ Sentence is **valid** according to the grammar. Root symbol '{start_symbol}' found in span [0,{n-1}].")
        return table
    else:
        print(f"\n❌ Sentence is **invalid**. Root symbol '{start_symbol}' not found in span [0,{n-1}].")
        return table

# --- Main Execution ---

if __name__ == "__main__":
    
    # Sentence 1: Valid
    input_sentence_valid = "The cat chased a dog"
    print(f"===== PARSING: '{input_sentence_valid}' =====")
    parse_sentence(input_sentence_valid, GRAMMAR)
    
    print("\n" + "="*50 + "\n")
    
    # Sentence 2: Invalid (A noun and a noun)
    input_sentence_invalid = "park cat dog"
    print(f"===== PARSING: '{input_sentence_invalid}' =====")
    parse_sentence(input_sentence_invalid, GRAMMAR)