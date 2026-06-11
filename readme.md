# 🧠 TextStat C L I

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> A fast, dependency-free Python terminal tool to analyze any text — by direct input or `.txt` file.

---

## 📸 Demo

```text
$ python analyzer.py

Enter file path (or press Enter to type text):
Paste your text below. Type END on a new line when done:
> Python is powerful and fun.
> It is used in AI, web, and data.
> Python developers are in high demand.
> END

🔍 TEXT ANALYSIS RESULT
----------------------------------------
Total characters (no spaces):  81
Total words:                   17
Unique words:                  14
Total sentences:               3

Top 5 most common words:
  python    ██████████  2
  is        ██████████  2
  and       ███████     2
  in        █████       1
  used      █████       1
```

---

## ⚙️ What It Analyzes

| Metric | Description |
|---|---|
| 🔤 Characters | Total count, excluding whitespace |
| 📝 Words | Full word count |
| 🔁 Unique Words | Distinct words (case-insensitive) |
| 🔢 Sentences | Detected via punctuation (`.` `!` `?`) |
| 🏆 Top 5 Words | Most frequent words with visual bar |

---

## ✨ Features

- **Direct input** — type or paste text in the terminal (multi-line supported)
- **File input** — load any `.txt` file by path
- **Visual frequency bar** — ASCII bar chart for top words
- **Clean, aligned output** — easy to read at a glance
- **Zero dependencies** — only Python standard library (`os`, `re`, `collections`)
- **Cross-platform** — Windows, macOS, Linux

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed ([Download here](https://www.python.org/downloads/))

### Installation

```bash
git clone https://github.com/yourusername/text-analyzer.git
cd text-analyzer
```

### Run

```bash
python analyzer.py
```

---

## 🎮 Usage

### Option A — Type or paste text

1. Press **Enter** when asked for a file path (leave it blank)
2. Type or paste your text (multi-line works)
3. Type `END` on a new line to submit

```text
Python is fun.
It makes coding easy.
Python is used for AI and web.
END
```

### Option B — Analyze a `.txt` file

1. Enter the path to your file when prompted (e.g., `sample.txt` or `docs/notes.txt`)
2. The script reads and analyzes it automatically

```bash
Enter file path (or press Enter to type text): sample.txt
```

---

## 📄 Sample Input (`sample.txt`)

```text
Python is fun to learn.
It makes coding simple and powerful.
Python is used for data, AI, and the web!
```

---

## 🗺️ Roadmap

### ✅ Done

- [x] Character, word, unique word, and sentence count
- [x] Top 5 most frequent words
- [x] Multi-line terminal input
- [x] `.txt` file input support

### 🔜 Coming Soon

- [ ] ASCII word-frequency bar chart (full)
- [ ] Longest & shortest words
- [ ] Average sentence length
- [ ] Reading time estimate (~200 wpm)
- [ ] Export results to `.txt` or `.csv`
- [ ] `--file` CLI flag for direct command-line usage

---

## 📂 Project Structure

```text
text-analyzer/
│
├── analyzer.py        # Core analysis logic + CLI interface
├── sample.txt         # Sample input file for quick testing
├── requirements.txt   # Empty — no external packages needed
└── README.md          # Documentation
```

---

## 🧩 Requirements

```text
Python 3.x
Standard library only: os, re, collections
No pip install needed
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create your branch:

```bash
git checkout -b feature/your-feature
```

3. Commit your changes:

```bash
git commit -m "feat: add your feature"
```

4. Push to the branch:

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

---

## 📋 Changelog

### v1.1.0

- Improved output formatting and alignment
- Added ASCII frequency bar for top words
- README fully rewritten with usage examples and roadmap

### v1.0.0

- Initial release
- Character, word, unique word, sentence count
- Top 5 most common words
- Direct input and `.txt` file support

---

## 💡 Tips

- Test with different text types — articles, code comments, essays
- Works in VS Code terminal, PowerShell, CMD, and any Unix shell
- Great base to extend with `nltk` or `spaCy` for NLP features

---

## 📜 License

MIT License — free to use, modify, and distribute.

Made with 🐍 Python.
