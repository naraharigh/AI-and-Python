from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import subprocess
import sys



def install_package(package_name):
    """Installs a Python package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

# Example usage:
install_package("scikit-learn")

pass

# 1. Load a pre-trained BERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# 2. Define your knowledge base (documents)
documents = [
    "The capital of France is Paris.",
    "Mount Everest is the highest mountain in the world.",
    "Python is a popular programming language.",
    "The Eiffel Tower is located in Paris."
]

# 3. Generate embeddings for the documents
def get_bert_embeddings(texts):
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the [CLS] token embedding as the sentence embedding
    return outputs.last_hidden_state[:, 0, :].numpy()

document_embeddings = get_bert_embeddings(documents)

# 4. Define a retrieval function
def retrieve_relevant_documents(query, doc_embeddings, docs, top_k=1):
    query_embedding = get_bert_embeddings([query])
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
    # Get indices of top_k most similar documents
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [docs[i] for i in top_indices]

# 5. Simulate a RAG query
query = "What is the capital of France?"
retrieved_docs = retrieve_relevant_documents(query, document_embeddings, documents)

print(f"Query: {query}")
print(f"Retrieved Documents: {retrieved_docs}")

# In a full RAG system, you would then pass these retrieved documents
# along with the query to a Large Language Model (LLM) for generation.
# For example, using a placeholder for the generation step:
def generate_response(query, context):
    # In a real RAG, this would involve an LLM
    return f"Based on the context '{context}', the answer to '{query}' is..."

generated_answer = generate_response(query, retrieved_docs[0])
print(f"Generated Answer: {generated_answer}")