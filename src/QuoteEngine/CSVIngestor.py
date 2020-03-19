""" Ingestor Module for `CSV` file formats """

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """ Ingestor Class for `CSV` file formats """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Ingests and parses `CSV` type files for quote extraction
        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List(QuoteModel) {List} -- List of QuoteModel objects.
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quote_models = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quote_models.append(new_quote)

        return quote_models
