import csv
import re
import subprocess
from docx import Document
from typing import List
from quote_model import QuoteModel

"""
This module provides several ingestion strategies for parsing quotes from different file formats, including PDF, CSV, TXT, and DOCX.
"""


class PDFIngestionStrategy():

    @staticmethod
    def parse(path) -> List[QuoteModel]:
        """
        Ingestion strategy for parsing quotes from PDF files.

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


class CsvIngestionStrategy():

    @staticmethod
    def parse(path) -> List[QuoteModel]:
        """
        Ingestion strategy for parsing quotes from CSV files.

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


class TxtIngestionStrategy():

    @staticmethod
    def parse(path) -> List[QuoteModel]:
        """
        Ingestion strategy for parsing quotes from plain text (TXT) files.

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


class DocxIngestionStrategy():

    @staticmethod
    def parse(path) -> List[QuoteModel]:
        """
        Ingestion strategy for parsing quotes from DOCX files.

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
