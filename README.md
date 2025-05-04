# Emoflagger

Emoflagger is a lightweight, privacy-conscious NLP application that performs sentiment and emotion classification on user-provided text using classical machine learning techniques.

It uses a Logistic Regression model trained on a public, ethically sourced dataset to detect whether a sentence expresses positive, neutral, or negative sentiment. It includes a simple web interface built with Flask and HTML.



---

## Showcase

### Positive Sentiment

<img src="showcase/positive_demo.png" width="600"/>

### Negative Sentiment

<img src="showcase/negative_demo.png" width="600"/>


---

## Features

- Text classification using `Logistic Regression`
- Clean and responsive web interface
- Displays sentiment label with confidence percentage
- Maintains prediction history during the session



---

## Dataset Used

- **Source**: [Sp1786/multiclass-sentiment-analysis-dataset (Hugging Face)](https://huggingface.co/datasets/Sp1786/multiclass-sentiment-analysis-dataset)
- Classes: `positive`, `neutral`, `negative`

---

## Tech Stack

- **Frontend**: HTML, JavaScript
- **Backend**: Flask (Python)
- **Modeling**: scikit-learn (TF-IDF + Logistic Regression)

---


