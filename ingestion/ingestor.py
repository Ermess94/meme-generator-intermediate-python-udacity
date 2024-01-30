from typing import List

from ingestion.model.quote_model import QuoteModel
from ingestion.pdf_ingestor import PDFIngestor
from ingestion.csv_ingestor import CSVIngestor
from ingestion.docx_ingestor import DocxIngestor
from ingestion.text_ingestor import TextIngestor


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
