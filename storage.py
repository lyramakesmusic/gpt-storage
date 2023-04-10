import openai
import json
from scipy.spatial.distance import cosine


class Storage:
    def __init__(self):
        self.storage = []

    def get_embedding(self, text: str) -> list:
        response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
        return response['data'][0]['embedding']

    def store(self, text: str) -> None:
        self.storage.append({"text": text, "embedding": self.get_embedding(text)})

    def best_match(self, query: str) -> str:
        query_embedding = self.get_embedding(query)
        min_distance = float("inf")
        match = None

        for entry in self.storage:
            distance = cosine(query_embedding, entry["embedding"])
            if distance < min_distance:
                min_distance = distance
                match = entry["text"]

        return match

    def save(self, file_name: str) -> None:
        with open(file_name, "w") as f:
            json.dump(self.storage, f)

    def load(self, file_name: str) -> None:
        with open(file_name, "r") as f:
            self.storage = json.load(f)
