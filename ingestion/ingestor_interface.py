from abc import ABC, abstractmethod
from typing import List

from ingestion.model.quote_model import QuoteModel


class IngestorInterface(ABC):
    """
    This abstract class defines the interface for creating different ingestion strategies for parsing quotes from various file formats.
    """

    @classmethod
    def can_ingest(self, path: str) -> bool:
        """
        Class method to check if the given file path can be ingested based on the file extension.

        Parameters:
            path (str): The path of the file to be checked.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        extension = path.split('.')[-1]
        valid_extensions = self.get_valid_extensions()
        return extension in valid_extensions

    @abstractmethod
    def get_valid_extensions(self):
        """
        An abstract method to be implemented by concrete ingestion strategy classes.
        Returns a list of valid file extensions that can be ingested.

        Returns:
            list: List of valid file extensions.
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
