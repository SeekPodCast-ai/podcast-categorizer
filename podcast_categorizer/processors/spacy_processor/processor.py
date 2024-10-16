from subprocess import run
from collections import Counter
import spacy
import os


class SpacyProcessor:
    def __init__(self):
        self.__model = os.environ["SPACY_MODEL_NAME"]
        try:
            self.__nlp = spacy.load(self.__model)
        except OSError:
            run(f"python -m spacy download {self.__model}", check=True, shell=True)
            self.__nlp = spacy.load(self.__model)

    def run(self, text: str):
        doc = self.__nlp(text)
        entities = [ent.text for ent in doc.ents]
        noun_chunks = [chunk.text for chunk in doc.noun_chunks]
        tags = list(set(entities + noun_chunks))
        tag_counts = Counter(tags).most_common()
        return entities, noun_chunks, tags, tag_counts
