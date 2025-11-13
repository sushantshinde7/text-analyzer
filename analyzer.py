import os
import re
from collections import Counter

def analyze_text(text):
    text = text.strip()
    words = re.findall(r'\b\w+\b', text.lower())
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]

    word_count = len(words)
    unique_words = len(set(words))
    char_count = len(text.replace(" ", ""))
    sentence_count = len(sentences)
    top_words = Counter(words).most_common(5)

    print("\n🔍 TEXT ANALYSIS RESULT")
    print("-" * 40)
    print(f"Total characters (no spaces): {char_count}")
    print(f"Total words: {word_count}")
    print(f"Unique words: {unique_words}")
    print(f"Total sentences: {sentence_count}")
    print("\nTop 5 most common words:")
    for word, count in top_words:
        print(f"  {word}: {count}")

def get_multiline_input(first_line=""):
    """
    Accepts multi-line text input until user enters 'END' on a new line.
    Includes the first line if provided.
    """
    lines = []
    if first_line:
        lines.append(first_line)
    print("Paste/type your text. Type 'END' on a new line to finish:")
    while True:
        try:
            line = input()
        except EOFError:
            # Handles Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) as end-of-input
            break
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("🧠 TEXT ANALYZER")
    print("-" * 30)
    choice = input("Enter a file path (.txt) or leave empty to type/paste text:\n> ").strip()

    text = ""
    if choice and os.path.isfile(choice):
        # read file
        with open(choice, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        # accept multi-line text directly
        text = get_multiline_input(first_line=choice)

    analyze_text(text)

if __name__ == "__main__":
    main()

