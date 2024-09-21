# Import necessary libraries
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load environment variables
load_dotenv()

# Load documents from a directory (you can change this path as needed)
documents = SimpleDirectoryReader("data").load_data()
# Print the number of documents
print(f"Number of documents loaded: {len(documents)}")

# Sample the first few documents (up to 3)
num_samples = min(3, len(documents))
print("\nSample of the first few documents:")
for i in range(num_samples):
    print(f"\nDocument {i + 1}:")
    print(f"Content: {documents[i].text[:200]}...")  # Print first 200 characters
    print(f"Metadata: {documents[i].metadata}")

# Create an index from the documents
index = VectorStoreIndex.from_documents(documents)

# Create a query engine
query_engine = index.as_query_engine()

# Example query
response = query_engine.query("What years does the strategic plan cover?")

print(response)