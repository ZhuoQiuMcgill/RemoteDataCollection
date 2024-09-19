import spacy
from spacy.pipeline import Sentencizer


class IndexedText:
    def __init__(self, text):
        """
        Initializes the IndexedText class with the given text.

        Args:
            text (str): The input text to be processed.

        Attributes:
            nlp (Language): The spaCy language model used for text processing.
            text (str): The original input text.
            doc (Doc): The processed spaCy document containing the text.
            punc (str): A string of punctuation characters used in processing.
            indexed_text (str): The text after indexing (initially empty).
            indexed_text_with_highlight (str): The indexed text with highlighted tokens (initially empty).
            number_of_sentences (int): The number of sentences in the text (initially 0).
            possible_tokens (list): A list of potential tokens found in the text (initially empty).
        """
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe("sentencizer")
        self.text = text
        self.doc = self.nlp(text)
        self.punc = ",.?!~`<>()[]{}@#$%^&*/_-+=:;"
        self.indexed_text = ""
        self.indexed_text_with_highlight = ""
        self.number_of_sentences = 0
        self.possible_tokens = []
        self.indexing()

    def divide_sentences(self):
        """
        Divides the text into sentences.

        Returns:
            list: A list of sentences extracted from the text.
        """
        sents = [sent.text for sent in self.doc.sents]
        self.number_of_sentences = len(sents)
        return sents

    def get_number_of_sentences(self):
        """
        Gets the number of sentences in the text.

        Returns:
            int: The number of sentences.
        """
        return self.number_of_sentences

    def get_indexed_text(self):
        """
        Gets the indexed version of the text.

        Returns:
            str: The indexed text.
        """
        return self.indexed_text

    def get_possible_tokens(self):
        """
        Gets the list of possible tokens from the text.

        Returns:
            list: A list of possible tokens found in the text.
        """
        return self.possible_tokens

    def get_indexed_text_with_highlight(self):
        """
        Gets the indexed text with highlighted tokens.

        Returns:
            str: The indexed text with highlights.
        """
        return self.indexed_text_with_highlight

    def indexing(self):
        """
        Indexes the text by assigning position-based tags to each token in the sentences.
        It identifies and highlights specific tokens such as nouns, proper nouns, and pronouns.

        The method performs the following steps:
        1. Divides the text into sentences.
        2. Iterates over each sentence and tokenizes it.
        3. Creates indexed tokens by adding position information.
        4. Highlights certain types of tokens and stores them separately.

        This process populates the `indexed_text`, `indexed_text_with_highlight`, and `possible_tokens` attributes.

        Returns:
            None
        """
        sents = self.divide_sentences()

        for i, sent in enumerate(sents):
            doc = self.nlp(sent)
            indexed_tokens = []
            indexed_tokens_with_highlight = []

            for token in doc:
                if token.text not in self.punc:
                    indexed_token = token.text + f'-({i}, {len(indexed_tokens)})'
                    indexed_tokens.append(indexed_token)

                    if token.pos_ in ["NOUN", "PROPN", "PRON"]:
                        indexed_tokens_with_highlight.append(IndexedText.highlight_text(indexed_token))
                        self.possible_tokens.append(indexed_token)
                    else:
                        indexed_tokens_with_highlight.append(indexed_token)

            self.indexed_text += " ".join(indexed_tokens) + ". "
            self.indexed_text_with_highlight += " ".join(indexed_tokens_with_highlight) + ". "

    @staticmethod
    def highlight_text(text):
        """
        Highlights the provided text by wrapping it in HTML span tags with a red color style.

        Args:
            text (str): The text to be highlighted.

        Returns:
            str: The highlighted text as an HTML span element with red color.
        """
        return f'<span style="color: red;">{text}</span>'
