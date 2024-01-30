import re
import subprocess
from typing import List

from ingestion.ingestor_interface import IngestorInterface
from ingestion.model.quote_model import QuoteModel


class PDFIngestor(IngestorInterface):

    @classmethod
    def get_valid_extensions(self) -> List[str]:
        """
        Returns a list of valid file extensions that can be ingested.

        Returns:
            list: List of valid file extensions.
        """
        return ['pdf'] 

    @classmethod
    def parse(self, path) -> List[QuoteModel]:
        """
        Ingestor for parsing quotes from PDF files.

        Parameters:
            path (str): The path to the PDF file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances parsed from the PDF.
        """
        data = []
        result = subprocess.run(
            ["pdftotext", path, "-"], capture_output=True, text=True)

        if result.returncode == 0:
            content = result.stdout.split('\n')[0]
            pattern = r'"([^"]*)" - ([^"]*)'
            matches = re.findall(pattern, content)
            for match in matches:
                data.append(QuoteModel(f'"{match[0]}"', match[1]))
        else:
            print(
                f"Error while converting PDF to text. Exit code: {result.returncode}")

        return data
