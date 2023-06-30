import pywhatkit as pwk
from PIL import Image, ImageDraw, ImageFont

# टेक्स्ट निर्धारित करें
text = "नमस्ते, यह एक हस्तलिखित संदेश है!"
font_size = 40
font_path = "path/to/hindi_font.ttf"

# हस्तलिखित टेक्स्ट उत्पन्न करें
pwk.text_to_handwriting(text, "temp.png", rgb=(0, 0, 0))

image = Image.open("temp.png")

# हिंदी फ़ॉन्ट लोड करें
font = ImageFont.truetype(font_path, font_size)

# सफेद पृष्ठभूमि वाली एक खाली छवि बनाएं
image_hindi = Image.new("RGB", image.size, (255, 255, 255))
draw = ImageDraw.Draw(image_hindi)

# छवि पर हिंदी टेक्स्ट लिखें
draw.text((10, 10), text, font=font, fill=(0, 0, 0))

# नई छवि को दिखाएं
image_hindi.show()

# नई छवि को फ़ाइल में सहेजें
image_hindi.save("handwritten_hindi.png")
