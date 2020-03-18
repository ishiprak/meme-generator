class QuoteModel:


    def __init__(self, body, author):
        self.body = body.strip()
        self.author = author.strip()


    def __repr__(self):
        return f'"{self.body}" - {self.author}'
        