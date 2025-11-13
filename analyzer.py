import os
import re
from collections import Counter

def analyze_text(text):
    # Clean up and normalize text
    text = text.strip()
    words = re.findall(r'\b\w+\b', text.lower())  # all words
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]  # remove empty

    word_count = len(words)
    unique_words = len(set(words))
    char_count = len(text.replace(" ", ""))
    sentence_count = len(sentences)

    # Top 5 words
    top_words = Counter(words).most_common(5)

    # Print neatly
    print("\n🔍 TEXT ANALYSIS RESULT")
    print("-" * 40)
    print(f"Total characters (no spaces): {char_count}")
    print(f"Total words: {word_count}")
    print(f"Unique words: {unique_words}")
    print(f"Total sentences: {sentence_count}")
    print("\nTop 5 most common words:")
    for word, count in top_words:
        print(f"  {word}: {count}")


def main():
    print("🧠 TEXT ANALYZER")
    print("-" * 30)
    choice = input("Enter text directly or type a file path (.txt):\n> ").strip()

    if os.path.isfile(choice):
        try:
            with open(choice, "r", encoding="utf-8") as f:
                text = f.read()
            analyze_text(text)
        except Exception as e:
            print(f"⚠️ Error reading file: {e}")
    else:
        analyze_text(choice)


if __name__ == "__main__":
    main()
