""" Ingestor Module for `txt` file formats """

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """ Ingestor Class for `txt` file formats """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Ingests and parses `txt` type files for quote extraction
        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List(QuoteModel) {List} -- List of QuoteModel objects.
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quote_models = []
        quote_txt = open(path, "r")

        for line in quote_txt.readlines():
            if line != "" or len(line) != 0:
                quote = line.strip('\n\r').strip().split("-")
                body = quote[0].strip()
                author = quote[1].strip()
                new_quote = QuoteModel(body, author)
                quote_models.append(new_quote)

        return quote_models
