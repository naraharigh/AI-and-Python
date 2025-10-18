import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score


data = []
with open("trainingdata.txt", "r", encoding="utf-8") as f:
    for line in f:
        
        if not line:
            continue
        if " " not in line:
            print(f"Skipping bad line: {line}")
            continue
        line = line.strip()
        if line:
            label, text = line.split(" ", 1)
            data.append([int(label), text])

df = pd.DataFrame(data, columns=["label", "text"])
print(df.head())


print(df['label'])
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'],test_size=0.2, random_state=42)

print(y_train)

vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)


# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:", classification_report(y_test, y_pred))


uncategorized_docs = ["This is a document","this is another document","documents are seperated by newlines",]

uncat_tfidf = vectorizer.transform(uncategorized_docs)
predicted_labels = model.predict(uncat_tfidf)

for doc, label in zip(uncategorized_docs, predicted_labels):
    print(label)
