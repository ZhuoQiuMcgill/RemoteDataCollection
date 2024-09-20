import spacy


class NLPModelSingleton:
    """
    A singleton class that loads and provides access to a shared spaCy language model instance.
    This class uses a singleton pattern to ensure only one instance of the language model is loaded.

    Attributes:
        _instance (NLPModelSingleton): The singleton instance of the NLPModelSingleton class.
        _nlp (spacy.lang.en.English): The loaded spaCy language model instance.
    """
    _instance = None
    _nlp = None

    def __new__(cls):
        """
        Creates a new instance of NLPModelSingleton if it does not exist; otherwise, returns the existing instance.

        Returns:
            NLPModelSingleton: The singleton instance of the NLPModelSingleton class.
        """
        if cls._instance is None:
            cls._instance = super(NLPModelSingleton, cls).__new__(cls)
            cls._nlp = spacy.load("en_core_web_sm")
        return cls._instance

    @staticmethod
    def get_instance():
        """
        Retrieves the singleton instance of NLPModelSingleton, creating it if necessary.

        Returns:
            NLPModelSingleton: The singleton instance of the NLPModelSingleton class.
        """
        if NLPModelSingleton._instance is None:
            NLPModelSingleton._instance = NLPModelSingleton()
        return NLPModelSingleton._instance

    @property
    def nlp(self):
        """
        Provides access to the loaded spaCy language model.

        Returns:
            spacy.lang.en.English: The loaded spaCy language model instance.
        """
        return self._nlp


if __name__ == '__main__':
    model = NLPModelSingleton.get_instance()
