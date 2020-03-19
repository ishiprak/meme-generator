""" Ingestor Module for `Docx` file formats """

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """ Ingestor Class for `Docx` file formats """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Ingests and parses `Docx` type files for quote extraction
        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List(QuoteModel) {List} -- List of QuoteModel objects.
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quote_models = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                quote = para.text.strip().split("-")
                body = quote[0].strip()
                author = quote[1].strip()
                new_quote = QuoteModel(body, author)
                quote_models.append(new_quote)

        return quote_models
