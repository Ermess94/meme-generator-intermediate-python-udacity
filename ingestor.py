from typing import List
from ingestion_strategies import CsvIngestionStrategy, PDFIngestionStrategy, TxtIngestionStrategy, DocxIngestionStrategy
from ingestor_interface import IngestorInterface
from quote_model import QuoteModel


class Ingestor(IngestorInterface):
    """
    This class provides functionality for ingesting quotes from different file formats such as PDF, CSV, TXT, and DOCX.
    It implements the IngestorInterface and uses various ingestion strategies for parsing the content of different file types.
    """

    @classmethod
    def can_ingest(self, path: str) -> bool:
        """
        Checks if the given file path can be ingested based on its extension.

        Parameters:
            path (str): The path of the file to be ingested.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        valid_extensions = ['pdf', 'csv', 'txt', 'docx']
        extension = path.split('.')[-1]
        if extension in valid_extensions:
            return True
        return False
    
    @classmethod
    def parse(self, path: str) -> List[QuoteModel]:
        """
        Parses the content of the file specified by the given path using the appropriate ingestion strategy.
        Returns a list of QuoteModel instances.

        Parameters:
            path (str): The path of the file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances parsed from the file.
        """
        extension = path.split('.')[-1]
        if extension == 'pdf':
            return PDFIngestionStrategy().parse(path)
        if extension == 'csv':
            return CsvIngestionStrategy().parse(path)
        if extension == 'txt':
            return TxtIngestionStrategy().parse(path)
        if extension == 'docx':
            return DocxIngestionStrategy().parse(path)
        return None
