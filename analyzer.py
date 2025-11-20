import os
import re
from collections import Counter


# -----------------------------
# TEXT ANALYSIS LOGIC
# -----------------------------
def analyze_text(text):
    text = text.strip()

    # Extract words & sentences
    words = re.findall(r'\b\w+\b', text.lower())
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]

    # Basic metrics
    word_count = len(words)
    unique_words = len(set(words))
    char_count = len(text.replace(" ", ""))
    sentence_count = len(sentences)
    top_words = Counter(words).most_common(5)

    # Output
    print("\n🔍 TEXT ANALYSIS RESULT")
    print("-" * 40)
    print(f"Total characters (no spaces): {char_count}")
    print(f"Total words: {word_count}")
    print(f"Unique words: {unique_words}")
    print(f"Total sentences: {sentence_count}")

    print("\nTop 5 most common words:")
    for word, count in top_words:
        print(f"  {word}: {count}")


# -----------------------------
# MULTILINE INPUT HANDLING
# -----------------------------
def get_multiline_input(first_line=""):
    """
    Accepts multi-line input until the user presses Enter twice.
    Works naturally for typing and pasting text.
    """
    print("Type or paste your text (press Enter twice to finish):\n")

    lines = []
    if first_line.strip():
        lines.append(first_line)

    empty_lines = 0

    while True:
        line = input()

        # Two empty lines = finish input
        if line.strip() == "":
            empty_lines += 1
            if empty_lines == 2:
                break
        else:
            empty_lines = 0

        lines.append(line)

    return "\n".join(lines)


# -----------------------------
# MAIN PROGRAM FLOW
# -----------------------------
def main():
    print("🧠 TEXT ANALYZER")
    print("-" * 30)

    file_input = input("Enter a file path (.txt) or leave empty to type/paste text:\n> ").strip()

    # Case 1 → File provided & exists
    if file_input and os.path.isfile(file_input):
        try:
            with open(file_input, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print(f"\n❌ Error reading file: {e}")
            return

    # Case 2 → User enters text manually (single or multi-line)
    else:
        text = get_multiline_input(first_line=file_input)

    analyze_text(text)


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()

