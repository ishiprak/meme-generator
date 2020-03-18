from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:

    def __init__(self, output_dir):
        self.out_path=output_dir


    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a Meme With a Quote captioned on it

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the body text for the caption quote.
            author {str} -- the author for the caption quote.
            width {int} -- the desired width for the output image {defaults to 500}.
        Returns:
            str -- the file path to the output image.
        """

        img = Image.open(img_path)
        quote = f'{text} - {author}'

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if quote is not None:
            draw = ImageDraw.Draw(img)
            font_list = ["../_data/fonts/BalooChettan2-Bold.ttf", "../_data/fonts/BalooChettan2-ExtraBold.ttf", 
                         "../_data/fonts/BalooChettan2-SemiBold.ttf", "../_data/fonts/BalooChettan2-Medium.ttf", 
                         "../_data/fonts/BalooChettan2-Regular.ttf"]
            font_type = random.choice(font_list)
            font = ImageFont.truetype(font_type, size=20)
            x=random.randint(0,300)
            y=random.randint(0,300)
            draw.text((x, y), quote, font=font, fill='white')


        img.save(self.out_path)
        return self.out_path
