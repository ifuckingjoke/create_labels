import os
from PIL import Image, ImageDraw, ImageFont
from .dict import FA_ICONS, DEFAULT_ICON
from .render import GenIcon

BASE_DIR = os.path.dirname(__file__)
FONT_PATH = os.path.join(BASE_DIR, "fonts", "fa-brands-400.woff2")
CACHE_DIR = os.path.join(BASE_DIR, "_cache")

def get_ico(domain, size=64):
    char = FA_ICONS.get(domain, DEFAULT_ICON)
    if not char:
        return None
    
    os.makedirs(CACHE_DIR, exist_ok=True)

    version = "v2"
    color = GenIcon.get_color(domain).replace("#", "")

    ico_name = f"{domain.split('.')[0]}_{version}_{color}.ico"
    ico_path = os.path.join(CACHE_DIR, ico_name)


    if os.path.exists(ico_path):
        return ico_path
    
    font = ImageFont.truetype(FONT_PATH, size)

    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    
    bbox = draw.textbbox((0,0), char, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    draw.text(
        ((size - w) // 2, (size - h) // 2),
        char,
        font=font,
        fill=GenIcon.get_color(domain)
    ) 

    img.save(ico_path, format="ICO")
    return ico_path