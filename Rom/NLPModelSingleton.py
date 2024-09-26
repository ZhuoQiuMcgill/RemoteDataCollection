import spacy
import coreferee


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
            if 'coreferee' not in cls._nlp.pipe_names:
                cls._nlp.add_pipe('coreferee', last=True)
            print(f'Spacy load model success! Current pipe names: {cls._nlp.pipe_names}')
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

    @staticmethod
    def extract_coreference_groups(doc):
        """
        Extracts coreference groups from the given doc and organizes tokens into separate lists for each group.

        Args:
            doc (spacy.tokens.Doc): The parsed document containing coreferences.

        Returns:
            list of list: A list containing lists of tokens that share the same coreference group,
                          with PROPN or NOUN tokens placed first if present.
        """
        coref_clusters = []  # To store all coreference groups

        # Check if coreference chains exist
        if not doc._.coref_chains:
            return coref_clusters

        # Iterate over each coreference chain
        for chain in doc._.coref_chains:
            chain_tokens = []  # To store tokens for the current chain
            nouns = []  # List to store PROPN or NOUN tokens
            others = []  # List to store other tokens

            # Iterate over each mention in the chain
            for mention in chain:
                # Extract tokens using indexes from mention
                tokens = [doc[i] for i in mention]
                # Separate PROPN/NOUN tokens and other tokens
                for token in tokens:
                    if token.pos_ in {"PROPN", "NOUN"}:
                        nouns.append(token)
                    else:
                        others.append(token)

            # Combine nouns first, followed by other tokens
            chain_tokens.extend(nouns + others)
            # Add the current chain list to the overall list
            coref_clusters.append(chain_tokens)

        return coref_clusters

    @staticmethod
    def split_into_sentences(text):
        """
        Splits the given text into a list of sentences with minimal processing.

        Args:
            text (str): The input text to be split into sentences.

        Returns:
            list: A list of sentences extracted from the input text.
        """
        nlp = spacy.blank("en")
        nlp.add_pipe("sentencizer")

        doc = nlp(text)
        sentences = [sent.text for sent in doc.sents]
        return sentences
