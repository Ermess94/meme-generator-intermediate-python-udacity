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
