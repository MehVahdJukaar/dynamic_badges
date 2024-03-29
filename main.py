import os
import threading
import time

from io import BytesIO

from github import Github

import pytesseract
import shutil
import requests

from PIL import Image, ImageDraw, ImageFont
from wand.image import Image as WandImage

github_password = os.environ.get('GITHUB_TOKEN')
github_user = "MehVahdJukaar"
repository_name = "dynamic_badges"


class Badge:
    def __init__(self, url, name, crop_box, old_text, new_text):
        self.url = url
        self.name = name
        self.crop_box = crop_box
        self.old_text = old_text
        self.new_text = new_text

    def background(self):
        return self.name + "_template.svg"

    def target(self):
        return self.name + ".svg"


# url, name, crop box
badges = [
    Badge(
        "https://img.shields.io/discord/790151253144895508?label=&color=2d2d2d&labelColor=dddddd&style=for-the-badge&logo=Discord",
        "discord", (140, 0, 340, 120), "Online 1000", "{} Online"),
    Badge(
        "https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%3Fusername%3Dmehvahdjukaar%26type%3Dpatrons&style=for-the-badge&label=&color=2d2d2d&labelColor=dddddd&",
        "patreon", (140, 0, 290, 120), "Supporters 20", "{} Supporters"
    ),
    Badge(
        "https://img.shields.io/youtube/channel/subscribers/UCOaLLgwzOdbH6rCI7izCptw?label=&color=2d2d2d&labelColor=dddddd&style=for-the-badge&logo=Youtube&message=Twitter&logoColor=ff0000",
        "youtube", (140, 0, 400, 120), "Subscribers 1k", "{} Subscribers"
    )
]


def download_and_read_image(url, name):
    try:

        # Send a GET request to download the image
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Read the image data
        image_data = response.content

        # push_to_git(image_data, name+"_received.svg")

        # Convert SVG to PNG using Wand
        # Convert SVG to PNG using Wand
        with WandImage(blob=image_data, format="svg", height=120, width=600) as img:  # Specify desired width and height
            img.format = "png"
            png_data = img.make_blob()

        # Open the PNG image using PIL
        image = Image.open(BytesIO(png_data))

        print("Image format:", image.format)
        print("Image size:", image.size)
        print("Image mode:", image.mode)

        return image
    except Exception as e:
        print("Error downloading/reading image:", e)
        return None


def parse_number_from_image(image, crop_box):
    try:
        # Crop the image to the specified box
        cropped_image = image.crop(crop_box)
        # cropped_image.show()
        # Perform OCR on the cropped image
        # Grayscale image

        parsed_text = pytesseract.image_to_string(cropped_image, config='--psm 6 -c tessedit_char_whitelist=0123456789.mk', lang='eng')
        # Remove non-numeric characters and convert to integer

        filtered = ''.join([char for char in parsed_text if char.isdigit() or char.lower() in ('k', 'm', '.')])

        if filtered == "":
            print("Error parsing number from image. Got <"+parsed_text+">")
            return None

        return filtered
    except Exception as e:
        print("Error parsing number from image:", e)
        return None


def replace_svg_text(target_image, old_string, new_string):
    try:
        # Open the SVG file
        with open(target_image, 'r') as file:
            svg_content = file.read()

        # Replace the old string with the new one
        modified_svg_content = svg_content.replace(old_string, new_string)

        return modified_svg_content

    except FileNotFoundError:
        print("Input SVG file not found.")
    except Exception as e:
        print("An error occurred:", e)


def push_to_git(file_content, file_path):
    try:
        # Create a PyGithub instance using the token
        g = Github(github_user, github_password)

        # Get the specified repository
        repo = g.get_user().get_repo(repository_name)

        # Create or update the file in the repository
        try:
            contents = repo.get_contents(file_path)

            # If file exists, update its content
            repo.update_file(file_path, "Updated " + file_path, file_content, contents.sha)
            print("File updated successfully in the repository:", repository_name)
        except:
            # If file doesn't exist, create it
            repo.create_file(file_path, "Created " + file_path, file_content)
            print("File created successfully in the repository:", repository_name)


    except Exception as e:
        print("An error occurred:", e)


def create_new_image(number):
    # Load the background image
    background_image = Image.open("background_image.png")  # Replace "background_image.jpg" with your image path

    # Define text properties
    text = "Your Text " + str(number)
    text_color = (255, 255, 255)  # RGB color tuple (white in this example)
    text_position = (100, 100)  # Position of the top-left corner of the text (adjust as needed)
    text_size = 40  # Font size of the text (adjust as needed)

    # Load a font (adjust the font path as needed)
    font = ImageFont.truetype("arial.ttf", text_size)

    # Create a drawing context
    draw = ImageDraw.Draw(background_image)

    # Draw the text on the background image
    draw.text(text_position, text, fill=text_color, font=font)

    # Save the resulting image
    background_image.save("output_image.png")

    background_image.show()  # Replace "output_image.jpg" with your desired output file path


def save(target_image):
    with open("temp.svg", 'w') as file:
        file.write(target_image)


def update_add_badges():
    #print("Hello from new thread")

    for badge in badges:
        # Download and read the Discord badge image
        discord_badge_image = download_and_read_image(badge.url, badge.name)

        if discord_badge_image:

            parsed_number = parse_number_from_image(discord_badge_image, badge.crop_box)

            if parsed_number is not None:
                print("Parsed number:", parsed_number)

                new_svg = replace_svg_text(badge.background(), badge.old_text, badge.new_text.format(parsed_number))

                # save(new_svg)

                push_to_git(new_svg, badge.target())

            else:
                print("Failed to parse number from the image.")
        else:
            print("Failed to download/read the image.")

    print("Over and out o7")


if __name__ == "__main__":
  
  while True:
      interval_hours = 1
      # Run the function
      #threading.Thread(target=update_add_badges).start()
      # Wait for the specified interval

      update_add_badges()

      break

      #print("Sleeping")
      #time.sleep(interval_hours * 3600)
