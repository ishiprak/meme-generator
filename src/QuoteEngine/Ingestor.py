"""Ingestor Encapsulating Module for different file formats"""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor


class Ingestor(IngestorInterface):
    """ Ingestor Encapsulating Class for different file formats """

    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Ingests and parses different file-formats for quote extraction
        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List(QuoteModel) {List} -- List of QuoteModel objects.
        """

        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
