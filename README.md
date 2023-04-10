# gpt-storage

A Python package for storing text chunks with their embeddings and retrieving the best-matching text for a given query using OpenAI's text embeddings API.
gpt-storage

## Setup

To install gpt-storage, clone the GitHub repository and install the package locally:

```bash
git clone https://github.com/lyramakesmusic/gpt-storage.git
cd gpt-storage
pip install -e .
```

To securely manage your OpenAI API token, use the `dotenv` library (install with `pip install python-dotenv`). Create a `.env` file in your project's root directory with your token: 

`OPENAI_API_KEY=your_openai_api_token`
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
```

## Usage

After installation, you can use the Storage class provided by gpt-storage to store text and embeddings, find the best match for a query, and save/load storage data to/from a JSON file.

Example Usage
```py
from gpt_storage.storage import Storage

# Create a Storage instance
storage = Storage()

# Store text chunks along with their embeddings
storage.store("Text about programming")
storage.store("Text about machine learning")
storage.store("Text about AI")

# Find the best match for a query
query = "Tell me something about deep learning."
best_match = storage.best_match(query)
print("Best matching text:", best_match)

# Save storage data to a JSON file
storage.save("storage.json")

# Load storage data from a JSON file
storage.load("storage.json")
```
