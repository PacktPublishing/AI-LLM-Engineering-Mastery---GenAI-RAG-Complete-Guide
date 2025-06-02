from PIL import Image, ImageDraw, ImageFont
import os


def add_text_watermark_to_folder(
    input_dir, out_dir, watermark_text, position, font_size=30
):

    # Create output directory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            image_path = os.path.join(input_dir, filename)
            original = Image.open(image_path)
            width, height = original.size

            # Create ImageDraw object
            draw = ImageDraw.Draw(original)

            # Set up font
            font = ImageFont.truetype("super_nought.ttf", size=font_size)

            # Get the text dimensions
            text_width = font.getmask(watermark_text).getbbox()[2]
            text_height = font.getmask(watermark_text).getbbox()[3]
            print(f"text width {text_width}, {text_height}")

            margin = 100

            # Get the coord to place the watermark in the bottom right corner
            a = width - text_width - margin
            b = height - text_height - margin

            # Apply the watermark
            draw.text((a, b), text=watermark_text, fill="white", font=font)

            # Save the watermarked image in the output directory
            # /output_dir/watermarked_adi-goldstein
            output_path = os.path.join(out_dir, f"watermarked_{filename}")

            original.save(output_path)
            print(f"Watermarked image saved as {output_path}")


input_directory = "./input_dir"
output_directory = "./output_dir"
watermak = "@vincibits"

add_text_watermark_to_folder(
    input_dir=input_directory,
    out_dir=output_directory,
    watermark_text=watermak,
    position=(50, 50),
    font_size=199,
)
