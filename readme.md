# 🧠 NLP Text Preprocessing Pipeline

This project demonstrates a simple and effective text preprocessing pipeline using **Python** and the **Natural Language Toolkit (NLTK)**.

It is designed for beginners to understand how raw text is cleaned and prepared before applying NLP or Machine Learning models.

---

## 🚀 Features

* Convert text to lowercase
* Remove punctuation manually
* Tokenize text using NLTK
* Remove common stopwords
* Step-by-step output visualization
* Automatic NLTK resource handling (downloads only if missing)

---

## 🛠️ Technologies Used

* Python 3
* NLTK (Natural Language Toolkit)

---

## 📂 Project Structure

```bash
text_preprocessing.py   # Main script
README.md              # Project documentation
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/tanmayayayy/Tokenizer.git
cd Tokenizer
```

Install dependencies:

```bash
pip install nltk
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Enter any text when prompted:

```bash
Enter text: Hello! This is a simple test sentence.
```

---

## 🔍 Example Output

```
Original Text:
Hello! This is a simple test sentence.

Lowercased:
hello! this is a simple test sentence.

Without Punctuation:
hello this is a simple test sentence

Tokens:
['hello', 'this', 'is', 'a', 'simple', 'test', 'sentence']

After Stopword Removal:
['hello', 'simple', 'test', 'sentence']
```

---

## 🧩 How It Works

### 🔡 Lowercasing

Converts all characters to lowercase to maintain uniformity.

### ✂️ Punctuation Removal

Removes punctuation characters manually using string processing.

### 🔤 Tokenization

Splits text into individual words using NLTK’s `word_tokenize`.

### 🚫 Stopword Removal

Filters out common words (like *is*, *the*, *and*) that do not add significant meaning.

---

## 📦 NLTK Resource Handling

The script automatically checks and downloads required NLTK resources:

* `punkt`
* `punkt_tab`

This ensures smooth execution without manual setup.

---

## 🎯 Use Cases

* Learning NLP preprocessing pipelines
* Educational demonstrations
* Preparing data for:

  * Machine Learning models
  * Sentiment analysis
  * Text classification

