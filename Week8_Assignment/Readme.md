# Text Preprocessing in Natural Language Processing

## Overview
This project demonstrates basic **text preprocessing techniques** used in Natural Language Processing (NLP).  
The program processes two paragraphs of text and applies multiple preprocessing steps to clean and normalize the data before analysis.

Text preprocessing is an important step in NLP because raw text often contains punctuation, stop words, and different word forms that may reduce the efficiency of machine learning models.

---

## Input
The program takes **two paragraphs of text** containing multiple punctuation marks such as:

. , : ; ! ?

These punctuation marks are removed during preprocessing.

---

## Preprocessing Techniques Implemented

### 1. Removing Punctuation
All punctuation marks are removed from the text using **Regular Expressions (Regex)**.

Example:

**Before**

Hello, how are you?

**After**

Hello how are you


---

### 2. Stop Word Removal
Stop words are common words that usually do not carry important meaning in text analysis.

Examples of stop words:

- is
- the
- and
- from
- to
- of

These words are removed to focus only on meaningful words.

---

### 3. Stemming
Stemming reduces words to their **root form** by removing suffixes.

Examples:

| Original Word | Stemmed Word |
|---------------|-------------|
| transforming | transform |
| machines | machin |
| decisions | decis |
| technologies | technolog |

Stemming may sometimes produce non-dictionary words but helps reduce word variations.

---

### 4. Lemmatization
Lemmatization converts words to their **base dictionary form (lemma)**.

Examples:

| Original Word | Lemma |
|---------------|-------|
| machines | machine |
| decisions | decision |
| responses | response |
| technologies | technology |

Lemmatization produces meaningful dictionary words and is generally more accurate than stemming.

---

## Technologies Used

- Python
- NLTK (Natural Language Toolkit)
- Regular Expressions (Regex)

---

## Required Libraries

Install the required libraries using:

```bash
pip install nltk