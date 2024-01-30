from typing import List
from ingestion import IngestorInterface, QuoteModel

class TextIngestor(IngestorInterface):

    @classmethod
    def get_valid_extensions(self) -> List[str]:
        """
        Returns a list of valid file extensions that can be ingested.

        Returns:
            list: List of valid file extensions.
        """
        return ['txt'] 

    @classmethod
    def parse(self, path) -> List[QuoteModel]:
        """
        Ingestor for parsing quotes from plain text (TXT) files.

        Parameters:
            path (str): The path to the TXT file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances parsed from the TXT file.
        """
        data = []
        with open(path, 'r', encoding='utf-8') as txtfile:
            for line in txtfile:
                parts = line.strip().split(' - ')
                data.append(QuoteModel(f'"{parts[0]}"', parts[1]))
        return data
