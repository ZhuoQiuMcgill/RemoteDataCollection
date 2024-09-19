import spacy

class NLPModelSingleton:
    _instance = None
    _nlp = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NLPModelSingleton, cls).__new__(cls)
            cls._nlp = spacy.load("en_core_web_sm")
        return cls._instance

    @staticmethod
    def get_instance():
        if NLPModelSingleton._instance is None:
            NLPModelSingleton._instance = NLPModelSingleton()
        return NLPModelSingleton._instance

    @property
    def nlp(self):
        return self._nlp


if __name__ == '__main__':
    model = NLPModelSingleton.get_instance()

