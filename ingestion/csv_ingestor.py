import csv
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
        data = []
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)

            for row in csv_reader:
                body = row['body']
                author = row['author']
                data.append(QuoteModel(f'"{body}"', author))
        return data
