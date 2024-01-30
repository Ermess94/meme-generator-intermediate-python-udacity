import os
import time
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """
    This module provides a MemeEngine class for generating memes by adding text and author attribution to images. 
    """

    def __init__(self, output_path) -> None:
        """
        Initializes the MemeEngine instance.

        Parameters:
            output_path (str): The path where the generated memes will be saved.
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        self.output_path = output_path

    def resize_image(self, original_image, max_width=500) -> Image:
        """
        Resizes the input image while maintaining its aspect ratio.

        Parameters:
            original_image (Image): The original image to be resized.
            max_width (int): The maximum width of the resized image (default is 500).

        Returns:
            Image: The resized image.
        """
        width, height = original_image.size
        new_width = min(width, max_width)
        new_height = int((new_width / width) * height)

        return original_image.resize(
            (new_width, new_height), Image.ADAPTIVE)

    def make_meme(self, img_path, text, author, width=500) -> None:
        """
        Generates a meme by adding text and author attribution to the input image and saves it to the output directory.

        Parameters:
            img_path (str): The path to the input image.
            text (str): The text to be added to the meme.
            author (str): The author attribution for the meme.
            width (int): The desired width of the meme (default is 500).

        Returns:
            Image: The created meme image path.
        """
        original_image = Image.open(img_path)
        original_image_name = original_image.filename.split("/")[-1]

        draw = ImageDraw.Draw(original_image)

        text_font = ImageFont.truetype("./OpenSans-Regular.ttf", 20)
        author_font = ImageFont.truetype("./OpenSans-Regular.ttf", 15)
        text_color = (255, 255, 255)

        height = original_image.height

        draw.text((10,  height - 80), f'{text}',
                  font=text_font, fill=text_color)
        draw.text((10, height - 50), f'- {author}',
                  font=author_font, fill=text_color)

        edited_image_path = f'{self.output_path}/{time.time()}_{original_image_name}'
        self.resize_image(original_image).save(edited_image_path)
        return edited_image_path
