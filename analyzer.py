import os
import re
from collections import Counter


# -----------------------------
# TEXT ANALYSIS LOGIC
# -----------------------------
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

    # --- NEW FEATURES BELOW ---
    longest_word = max(words, key=len) if words else ""
    shortest_word = min(words, key=len) if words else ""
    avg_sentence_length = word_count / sentence_count if sentence_count else 0

    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Average sentence length: {avg_sentence_length:.2f} words")
    print("\nTop 5 most common words:")
    for word, count in top_words:
        print(f"  {word}: {count}")

    print("\nWord Frequency Bar Graph:")
    print("-" * 40)
    for word, count in top_words:
        print(f"{word:10} | {'#' * count}")



# -----------------------------
# MULTILINE INPUT HANDLING
# -----------------------------
def get_multiline_input(first_line=""):
    print("Add more lines if needed. Press Enter once for a new line, or press Enter twice to finish:\n")

    lines = []
    empty_count = 0

    # Only add first_line if it contains text
    if first_line.strip():
        lines.append(first_line)

    while True:
        line = input()

        # Two empty lines = finish input
        if line.strip() == "":
            empty_count += 1
            if empty_count == 2:
                break
        else:
            empty_count = 0
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

