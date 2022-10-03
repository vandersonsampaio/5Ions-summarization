from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer as Lsa


class SummarizeService:

    def __init__(self):
        pass

    @staticmethod
    def summarize(content, language):
        parser = PlaintextParser.from_string(content, Tokenizer(language))
        lsa = Lsa()

        summary = lsa(parser.document, "30%")

        text = ""
        for sentence in summary:
            text = str(text) + str(sentence)

        return text
