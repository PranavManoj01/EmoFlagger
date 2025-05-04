from datasets import load_dataset

# Load the dataset from the Hugging Face Hub
# This will automatically download and cache the dataset
dataset = load_dataset("Sp1786/multiclass-sentiment-analysis-dataset")

# You can print the dataset object to see its structure
print(dataset)

import nltk
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords')