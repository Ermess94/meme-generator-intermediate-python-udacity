from typing import List
from docx import Document

from ingestion import IngestorInterface, QuoteModel


class DocxIngestor(IngestorInterface):

    @classmethod
    def get_valid_extensions(self) -> List[str]:
        """
        Returns a list of valid file extensions that can be ingested.

        Returns:
            list: List of valid file extensions.
        """
        return ['docx'] 

    @classmethod
    def parse(self, path) -> List[QuoteModel]:
        """
        Ingestor for parsing quotes from DOCX files.

        Parameters:
            path (str): The path to the DOCX file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances parsed from the DOCX file.
        """
        data = []
        doc = Document(path)
        for paragraph in doc.paragraphs:
            if len(paragraph.text.strip()) > 0:
                parts = paragraph.text.split(' - ')
                data.append(QuoteModel(parts[0], parts[1]))
        return data
