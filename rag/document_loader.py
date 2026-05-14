class DocumentLoader:
    """
    A simple document loader for reading local text files.
    """

    def load_text_file(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
