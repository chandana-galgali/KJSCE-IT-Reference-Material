import sys
import subprocess
import os
import re
from collections import Counter, defaultdict

# --- Helper: install missing packages ---
def ensure_pkg(pkg_name: str):
    try:
        __import__(pkg_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
        __import__(pkg_name)

ensure_pkg("nltk")
ensure_pkg("pandas")

import nltk
import pandas as pd

# --- Step 1: Download required NLTK resources ---
def ensure_nltk_data():
    resources = [
        ("corpora", "gutenberg"),
        ("corpora", "brown"),
        ("corpora", "reuters"),
        ("corpora", "stopwords"),
    ]
    for rtype, name in resources:
        try:
            nltk.data.find(f"{rtype}/{name}")
        except LookupError:
            nltk.download(name)

ensure_nltk_data()

from nltk.corpus import gutenberg, brown, reuters, stopwords
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer

# --- Step 2: Build a large corpus (Gutenberg + Brown + Reuters) ---
def build_large_corpus_text() -> str:
    texts = []
    # Gutenberg
    for fid in gutenberg.fileids():
        texts.append(gutenberg.raw(fid))
    # Brown (join words per category)
    for cat in brown.categories():
        words = brown.words(categories=cat)
        texts.append(" ".join(words))
    # Reuters (join words per file id)
    for fid in reuters.fileids():
        words = reuters.words(fid)
        texts.append(" ".join(words))
    return "\n".join(texts)

# --- Step 3: Preprocess (lowercase, alphabetic tokens, remove stopwords) ---
def preprocess(text: str):
    # simple regex tokenizer: keep only alphabetic sequences
    tokens = re.findall(r"[A-Za-z]+", text.lower())
    sw = set(stopwords.words("english"))
    tokens = [t for t in tokens if t not in sw and len(t) > 2]
    return tokens

# --- Step 4: Apply stemmers ---
def stem_with_all(tokens):
    porter = PorterStemmer()
    snowball = SnowballStemmer(language="english")  # ignore_stopwords not needed after removing them
    lancaster = LancasterStemmer()
    regexp = RegexpStemmer('ing$|s$|e$|able$', min=4)

    stems = {
        "porter": [porter.stem(t) for t in tokens],
        "snowball": [snowball.stem(t) for t in tokens],
        "lancaster": [lancaster.stem(t) for t in tokens],
        "regexp": [regexp.stem(t) for t in tokens],
    }
    return stems

# --- Utility: Summaries ---
def summarize(tokens, stems_dict):
    vocab_original = set(tokens)
    print("\n=== SIZE SUMMARY ===")
    print(f"Total tokens (after preprocessing): {len(tokens):,}")
    print(f"Unique tokens BEFORE stemming: {len(vocab_original):,}")

    rows = []
    for name, stems in stems_dict.items():
        vocab_stem = set(stems)
        reduction = 100.0 * (1 - (len(vocab_stem) / len(vocab_original)))
        rows.append([name, len(vocab_stem), f"{reduction:.2f}%"])
    df = pd.DataFrame(rows, columns=["Stemmer", "Unique tokens AFTER", "Vocab reduction vs. original"])
    print(df.to_string(index=False))
    return df

# --- Utility: Word → stems side-by-side table ---
def build_word_to_stems_table(tokens, stems_dict, max_words=5000):
    # We'll create a mapping for the most common words (to keep file size reasonable)
    freq = Counter(tokens)
    most_common_words = [w for w, _ in freq.most_common(max_words)]

    records = []
    for w in most_common_words:
        rec = {"word": w}
        for name, stems in stems_dict.items():
            # find the first occurrence of w and pick its stem (consistent for same word)
            # more efficient: compute once a word->stem map for each stemmer
            rec[name] = None
        records.append(rec)

    # Precompute per-stemmer word->stem maps
    maps = {}
    for name, stems in stems_dict.items():
        mapping = {}
        for tok, st in zip(tokens, stems):
            if tok not in mapping:
                mapping[tok] = st
        maps[name] = mapping

    for rec in records:
        w = rec["word"]
        for name, mapping in maps.items():
            rec[name] = mapping.get(w, "")

    df = pd.DataFrame.from_records(records, columns=["word", "porter", "snowball", "lancaster", "regexp"])
    return df

# --- Utility: Collisions (potential over-stemming evidence) ---
def find_collisions(tokens, stems):
    # Map stem -> set(words) that produced it
    coll = defaultdict(set)
    for w, s in zip(tokens, stems):
        coll[s].add(w)
    # Keep stems that come from 2+ different words
    collisions = {stem: ws for stem, ws in coll.items() if len(ws) >= 2}
    # Rank by how many distinct words collapsed
    ranked = sorted(collisions.items(), key=lambda kv: len(kv[1]), reverse=True)
    return ranked

def collisions_to_dataframe(ranked, topn=50, stemmer_name=""):
    rows = []
    for stem, words in ranked[:topn]:
        # show up to 12 originals to keep row readable
        sample = ", ".join(list(sorted(words))[:12])
        rows.append([stemmer_name, stem, len(words), sample])
    df = pd.DataFrame(rows, columns=["stemmer", "stem", "distinct_original_words", "originals_sample"])
    return df

# --- Utility: Hand-checked pairs to illustrate under/over stemming ---
def inspect_examples(stem_fns):
    pairs_over = [
        ("universe", "university"),
        ("policy", "police"),
        ("general", "generation"),
        ("final", "finally"),
        ("organ", "organic"),
    ]
    pairs_under = [
        ("analysis", "analyst"),
        ("connect", "connection"),
        ("biology", "biological"),
        ("economy", "economic"),
        ("happy", "happiness"),
    ]
    print("\n=== CHECKED EXAMPLES (POTENTIAL OVER-STEMMING) ===")
    for a, b in pairs_over:
        row = [f"{a:<12} / {b:<12}"]
        for name, fn in stem_fns.items():
            row.append(f"{name}: {fn(a)} / {fn(b)}")
        print(" | ".join(row))

    print("\n=== CHECKED EXAMPLES (POTENTIAL UNDER-STEMMING) ===")
    for a, b in pairs_under:
        row = [f"{a:<12} / {b:<12}"]
        for name, fn in stem_fns.items():
            row.append(f"{name}: {fn(a)} / {fn(b)}")
        print(" | ".join(row))

def main():
    out_dir = "stemming_outputs"
    os.makedirs(out_dir, exist_ok=True)

    print("Building large corpus from Gutenberg + Brown + Reuters...")
    text = build_large_corpus_text()
    print("Preprocessing (lowercase, alphabetic only, remove stopwords, len>2)...")
    tokens = preprocess(text)

    print("Applying stemmers...")
    stems_dict = stem_with_all(tokens)

    # Summary metrics
    df_summary = summarize(tokens, stems_dict)
    df_summary.to_csv(os.path.join(out_dir, "summary_metrics.csv"), index=False)

    # Side-by-side word -> stems
    df_map = build_word_to_stems_table(tokens, stems_dict, max_words=5000)
    df_map.to_csv(os.path.join(out_dir, "word_to_stems_5k.csv"), index=False)
    print(f"\nSaved word-to-stems sample table to {os.path.join(out_dir, 'word_to_stems_5k.csv')}")

    # Collisions for each stemmer
    all_collisions = []
    for name, stems in stems_dict.items():
        ranked = find_collisions(tokens, stems)
        df_coll = collisions_to_dataframe(ranked, topn=100, stemmer_name=name)
        fp = os.path.join(out_dir, f"collisions_top100_{name}.csv")
        df_coll.to_csv(fp, index=False)
        all_collisions.append(df_coll)
        print(f"Saved top-100 collisions for {name} to {fp} (potential over-stemming examples).")

    # Print a small on-screen preview of collisions
    print("\n=== SAMPLE COLLISIONS (Top 10 per stemmer) ===")
    for dfc in all_collisions:
        print("\n--", dfc['stemmer'].iloc[0], "--")
        print(dfc.head(10).to_string(index=False))

    # Hand-checked pairs to illustrate over/under stemming cleanly
    porter = PorterStemmer()
    snowball = SnowballStemmer(language="english")
    lancaster = LancasterStemmer()
    regexp = RegexpStemmer('ing$|s$|e$|able$', min=4)
    stem_fns = {
        "porter": porter.stem,
        "snowball": snowball.stem,
        "lancaster": lancaster.stem,
        "regexp": regexp.stem,
    }
    inspect_examples(stem_fns)

    # Short narrative Observations (print to console + save)
    observations = []

    # Vocabulary reductions
    vocab_original = len(set(tokens))
    for name, stems in stems_dict.items():
        reduction = 100.0 * (1 - (len(set(stems)) / vocab_original))
        observations.append(f"{name.capitalize():<10} vocab reduction vs. original: {reduction:.2f}%")

    observations += [
        "",
        "Notes:",
        "- Lancaster is the most aggressive; expect more collisions (possible over-stemming).",
        "- Snowball is a refined version of Porter for English; typically balanced and multilingual in general.",
        "- Regexp only strips patterns you specify; safe but limited (may under-stem vs. algorithmic stemmers).",
        "- Over-stemming: different words collapsing to one stem (see collisions tables).",
        "- Under-stemming: related words kept apart (see checked examples like 'analysis' vs 'analyst').",
    ]
    obs_text = "\n".join(observations)
    print("\n=== OBSERVATIONS SUMMARY ===")
    print(obs_text)
    with open(os.path.join(out_dir, "observations.txt"), "w", encoding="utf-8") as f:
        f.write(obs_text)

    print(f"\nAll outputs saved under: {os.path.abspath(out_dir)}")
    print("Done.")

if __name__ == "__main__":
    main()