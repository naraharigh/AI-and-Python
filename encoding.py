# Enter your code here. Read input from STDIN. Print output to STDOUT


import sys
import subprocess

# Install scikit-learn if it's missing
subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn"])
# Install scikit-learn
# subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn"])
from sklearn.feature_extraction.text import CountVectorizer

# Read input lines from STDIN (until EOF)
lines = sys.stdin.read().strip().split("\n")

#Optional: Separate labels and text (if your format is: "label text...")
labels = []
texts = []
for line in lines:
    if not line.strip():
        continue
    label, text = line.split(" ", 1)
    labels.append(label)
    texts.append(text)

#Encode text using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
