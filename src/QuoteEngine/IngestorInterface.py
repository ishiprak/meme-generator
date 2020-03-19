"""Ingestor Base-Class Module for different file formats"""

from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """ Ingestor Abstract Base Class (ABC) for different file formats """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Base Class method for checking if Ingesting is possible
        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            bool {bool} -- Boolean value (True or False).
        """

        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method for Ingesting and parsing different file-formats
        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List(QuoteModel) {List} -- List of QuoteModel objects.
        """
        pass
