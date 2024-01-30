from typing import List
from ingestion import QuoteModel, PDFIngestor, CSVIngestor, DocxIngestor, TextIngestor


class Ingestor():

    @staticmethod
    def parse(path: str) -> List[QuoteModel]:
        """
        Parses the content of the file specified by the given path using the appropriate ingestion strategy.
        Returns a list of QuoteModel instances.

        Parameters:
            path (str): The path of the file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances parsed from the file.
        """

        ingestors = [PDFIngestor(), CSVIngestor(),
                     DocxIngestor(), TextIngestor()]

        for ingestor in ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise Exception("No suitable ingestor found for the specified file.")
