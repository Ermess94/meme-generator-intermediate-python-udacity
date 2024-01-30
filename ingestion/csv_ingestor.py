
import pandas as pd
from typing import List
from ingestion import IngestorInterface, QuoteModel

class CSVIngestor(IngestorInterface):

    @classmethod
    def get_valid_extensions(self) -> List[str]:
        """
        Returns a list of valid file extensions that can be ingested.

        Returns:
            list: List of valid file extensions.
        """
        return ['csv']

    @classmethod
    def parse(self, path) -> List[QuoteModel]:
        """
        Ingestior for parsing quotes from CSV files.

        Parameters:
            path (str): The path to the CSV file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances parsed from the CSV.
        """
        data = pd.read_csv(path, encoding='utf-8')
        quotes = []

        for index, row in data.iterrows():
            body = row['body']
            author = row['author']
            quotes.append(QuoteModel(f'"{body}"', author))

        return quotes
