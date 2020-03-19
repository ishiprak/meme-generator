""" Module for the processing of input image file to prepare Memes """
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    """ Class for the processing of input image file to prepare Memes """

    def __init__(self, output_dir):
        """ Overriding __init__ base class method for object instantiation
        Arguments:
            output_dir {str} -- output directory path for resultant meme.
        Returns:
            MemeEngine {object} -- MemeEngine object instant for given params
        """
        self.out_path = output_dir

    def image_resize(self, img, width):
        """ Create a Meme With a Quote captioned on it
        Arguments:
            img {PIL.Image object} -- Image object for the input image.
            width {int} -- desired width for the output image.
        Returns:
            img {PIL.Image object} -- Image object for resized output image.
        """
        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
            return img

    def draw_quote(self, img, quote):
        """ Draw Quote-texts over the image files for meme
        Arguments:
            img {PIL.Image object} -- Image object for the input image.
            quote {str} -- quote text for the caption quote.
        Returns:
            None
        """
        if quote is not None:
            draw = ImageDraw.Draw(img)
            font_type = "./_data/fonts/BungeeInline-Regular.ttf"
            font = ImageFont.truetype(font_type, size=25)
            x = random.randint(0, 35)
            y = random.randint(0, 350)
            draw.text((x, y), quote, font=font, fill='white')

    def make_meme(self, img_path: str, text: str, author: str, width=500):
        """ Create a Meme With a Quote captioned on it
        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the body text for the caption quote.
            author {str} -- the author for the caption quote.
            width {int} -- the desired width for the output image.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)
        quote = f'{text}\n   - {author}'
        img = self.image_resize(img, width)
        self.draw_quote(img, quote)
        img_path = self.out_path+f'/{random.randint(0,1000000)}.jpg'
        img.save(img_path)
        return img_path
