class SimpleRetriever:
    """
    A simple keyword-based retriever for demonstration.
    This is not an embedding-based retriever yet.
    """

    def retrieve(self, query: str, documents: list[str], top_k: int = 3) -> list[str]:
        scored_docs = []

        for doc in documents:
            score = doc.lower().count(query.lower())
            scored_docs.append((score, doc))

        scored_docs.sort(reverse=True, key=lambda x: x[0])

        return [doc for score, doc in scored_docs[:top_k] if score > 0]
