from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TextIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import CSVIngestor
from .CSVIngestor import CSVIngestor


class Ingestor(IngestorInterface):
    ingestors = [DocxImporter, CSVImporter, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
