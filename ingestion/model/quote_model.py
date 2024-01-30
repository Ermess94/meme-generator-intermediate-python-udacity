class QuoteModel():
    """
    This class represents a simple model for storing and managing textual quotes, including the quote body and author information.
    """

    def __init__(self, body, author) -> None:
        """
        Initializes the QuoteModel instance with the provided quote body and author.

        Parameters:
            body (str): The text of the quote.
            author (str): The author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """
        Returns a string representation of the QuoteModel instance.

        The returned string includes the quote body and author in the format:
        "{quote_body} - {author}"

        Returns:
            str: A string representation of the QuoteModel instance.
        """
        return f'{self.body} - {self.author}'
