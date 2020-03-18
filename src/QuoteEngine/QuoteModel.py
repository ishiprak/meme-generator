class QuoteModel:


    def __init__(self, text):
        quote = text.strip().split("-")
        self.body = quote[0].strip()
        self.author = quote[1].strip()


    def __repr__(self):
        return f'"{self.body}" - {self.author}'
        