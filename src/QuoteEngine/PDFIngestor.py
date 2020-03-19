""" Ingestor Module for `PDF` file formats """

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """ Ingestor Class for `PDF` file formats """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Ingests and parses `PDF` type files for quote extraction
        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List(QuoteModel) {List} -- List of QuoteModel objects.
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        temp_file = f'./tmp/{random.randint(0,10000)}.txt'
        call = subprocess.call(['pdftotext', path, temp_file])

        file_ref = open(temp_file, "r")
        quote_models = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0].strip(), parsed[1].strip())
                quote_models.append(new_quote)

        file_ref.close()
        os.remove(temp_file)
        return quote_models
