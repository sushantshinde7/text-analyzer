
# 🧠 Text Analyzer (Python)

A terminal-based Python tool that analyzes any text or `.txt` file.

It calculates:
- Total characters (excluding spaces)
- Total words
- Unique words
- Number of sentences
- Top 5 most common words

This project is beginner-friendly and demonstrates Python string handling, text analysis, and working with files.

---

## ⚙️ Features

- Analyze text typed or pasted directly (multi-line supported)
- Analyze text from `.txt` files
- Shows neat terminal output
- Easy to understand and extend
- Works on Windows, Mac, and Linux terminals

---

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/text-analyzer.git
cd text-analyzer
```

2. **Run the script**

```bash
python analyzer.py
```

3. **Provide input**  
Option 1: 
- Paste/type text directly
- Leave the file path blank → press Enter
- Paste/type multiple lines
- Type END on a new line to finish input

Example:
```bash
Python is fun.
It makes coding easy.
Python is used for AI and web.
END
```


Option 2: 
- Use a .txt file
- Type the file path (e.g., sample.txt) → press Enter
- The script reads the file and analyzes automatically

---

## 📊 Example Output

```text
🔍 TEXT ANALYSIS RESULT
----------------------------------------
Total characters (no spaces): 96
Total words: 20
Unique words: 15
Total sentences: 3

Top 5 most common words:
  python: 2
  is: 2
  coding: 1
  fun: 1
  learn: 1
```

---

## 📄 Sample Input File (`sample.txt`)

```text
Python is fun to learn.
It makes coding simple and powerful.
Python is used for data, AI, and the web!
```

---

## 🧩 Requirements

```text
Python 3.x
Built-in libraries only: os, re, collections
No external packages required
```

---

## 💡 Tips

- You can create multiple .txt files for testing different texts
- Multi-line input works by typing/pasting text and ending with END
- Works on any terminal: VS Code, PowerShell, CMD, Linux, Mac 
---

## 📂 Project Structure

```text
text-analyzer/
│
├─ analyzer.py        # main Python script
├─ sample.txt         # sample input file
├─ requirements.txt   # optional, empty
└─ README.md          # this file
```

---

## 📜 License

```text
MIT License
```


