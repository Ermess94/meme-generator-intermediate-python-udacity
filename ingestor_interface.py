from abc import ABC, abstractmethod
from typing import List
from quote_model import QuoteModel


class IngestorInterface(ABC):
    """
    This abstract class defines the interface for creating different ingestion strategies for parsing quotes from various file formats.
    """

    @abstractmethod
    def can_ingest(self, path: str) -> bool:
        """
        An abstract method to be implemented by concrete ingestion strategy classes.
        Checks if the given file path can be ingested.

        Parameters:
            path (str): The path of the file to be checked.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        pass

    @abstractmethod
    def parse(self, path: str) -> List[QuoteModel]:
        """
        An abstract method to be implemented by concrete ingestion strategy classes.
        Parses the content of the file specified by the given path and returns a list of QuoteModel instances.

        Parameters:
            path (str): The path of the file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances parsed from the file.
        """
        pass
