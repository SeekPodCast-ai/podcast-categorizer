from podcast_categorizer.processors.spacy_processor.processor import SpacyProcessor


class InvalidProcessorException(Exception):
    pass


class Categorizer:
    def __init__(self, processor: str) -> None:
        self.processor = processor
        self.__allowed_processors = ("spacy",)
        if self.processor not in self.__allowed_processors:
            raise InvalidProcessorException(
                f"Invalid Processor - {self.processor}. Valid inputs are - {self.__allowed_processors}"
            )

    def categorize(self, text):
        if self.processor == "spacy":
            spacy_processor = SpacyProcessor()
            return spacy_processor.run(text)
