# 🧠 Text Analyzer (Python — Terminal)

A lightweight, terminal-based Python tool that analyzes any text — either typed/pasted directly or loaded from a `.txt` file.

---

## ⚙️ What It Analyzes

| Metric | Description |
|---|---|
| 🔤 Characters | Total characters, excluding spaces |
| 📝 Words | Total word count |
| 🔁 Unique Words | Distinct words (case-insensitive) |
| 🔢 Sentences | Sentence count based on punctuation |
| 🏆 Top 5 Words | Most frequently used words |

---

## ✨ Features

- **Direct input** — paste or type text in the terminal (multi-line supported)
- **File input** — point to any `.txt` file for instant analysis
- **Clean output** — formatted, readable results in any terminal
- **Zero dependencies** — uses only Python built-in libraries
- **Cross-platform** — works on Windows, macOS, and Linux

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/text-analyzer.git
cd text-analyzer
```

### 2. Run the script

```bash
python analyzer.py
```

### 3. Choose your input method

**Option A — Type or paste text directly:**

- Leave the file path blank → press **Enter**
- Type or paste your text (multi-line supported)
- Type `END` on a new line to finish

```
Python is fun.
It makes coding easy.
Python is used for AI and web.
END
```

**Option B — Use a `.txt` file:**

- Enter the file path (e.g., `sample.txt`) → press **Enter**
- The script reads and analyzes the file automatically

---

## 📊 Example Output

```
🔍 TEXT ANALYSIS RESULT
----------------------------------------
Total characters (no spaces): 96
Total words:                   20
Unique words:                  15
Total sentences:               3

Top 5 most common words:
  python  ██████  2
  is      ██████  2
  coding  ███     1
  fun     ███     1
  learn   ███     1
```

---

## 📄 Sample Input (`sample.txt`)

```
Python is fun to learn.
It makes coding simple and powerful.
Python is used for data, AI, and the web!
```

---

## 🗺️ Roadmap

- [x] Character, word, unique word, sentence count
- [x] Top 5 most common words
- [ ] Longest & shortest words
- [ ] Average sentence length
- [ ] ASCII word-frequency bar chart
- [ ] Reading time estimate

---

## 📂 Project Structure

```
text-analyzer/
│
├── analyzer.py        # Main Python script
├── sample.txt         # Sample input file for testing
├── requirements.txt   # Empty — no external packages needed
└── README.md          # This file
```

---

## 🧩 Requirements

```
Python 3.x
Built-in libraries only: os, re, collections
No external packages required
```

---

## 💡 Tips

- Create multiple `.txt` files to batch-test different types of text
- Works in VS Code terminal, PowerShell, CMD, and any Unix shell
- Great starting point for extending with NLP features

---

## 📜 License

MIT License — free to use, modify, and distribute.
