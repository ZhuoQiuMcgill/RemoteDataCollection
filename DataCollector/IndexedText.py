import spacy
from spacy.pipeline import Sentencizer


class IndexedText:
    def __init__(self, text):
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
        sents = [sent.text for sent in self.doc.sents]
        self.number_of_sentences = len(sents)
        return sents

    def get_number_of_sentences(self):
        return self.number_of_sentences

    def get_indexed_text(self):
        return self.indexed_text

    def get_possible_tokens(self):
        return self.possible_tokens

    def get_indexed_text_with_highlight(self):
        return self.indexed_text_with_highlight

    def indexing(self):
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
        return f'<span style="color: red;">{text}</span>'

