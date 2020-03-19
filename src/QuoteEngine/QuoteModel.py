""" QuoteModel Module for instantiating QuoteModel objects """


class QuoteModel:
    """ QuoteModel Class for instantiating Quote-based objects """

    def __init__(self, body, author):
        """ Overriding __init__ base class method for object instantiation
        Arguments:
            body {str} -- body text for the QuoteModel.
            author {str} -- author for the QuoteModel.
        Returns:
            QuoteModel {object} -- QuoteModel object instant for given params
        """
        self.body = body.strip()
        self.author = author.strip()

    def __repr__(self):
        """ Overriding __repr__ base class method for object representation
        Arguments:
            None
        Returns:
            String {str} -- String representation of QuoteModel objects.
        """
        return f'"{self.body}" - {self.author}'
