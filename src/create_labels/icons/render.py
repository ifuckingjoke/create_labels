import tkinter as tk
from tkinter import font
from .dict import FA_ICONS, DEFAULT_ICON

class GenIcon:
    _font_cache = None

    @classmethod
    def get_font(cls, size=24):
        if cls._font_cache is None:
            cls._font_cache = font.Font(
                family="Font Awesome 6 Brands",
                size=size
            )
        return cls._font_cache

    @classmethod
    def get_glyph(cls, domain):
        return FA_ICONS.get(domain, DEFAULT_ICON)
    
    @classmethod
    def label(cls, parent, domain, size=24, **kwargs):
        return tk.Label(
            parent,
            text=cls.get_glyph(domain),
            font=cls.get_font(size),
            **kwargs
        )
    
    @staticmethod
    def get_color(domain):

        BRAND_COLORS = {
        # Search / general
        "google.com": "#4285F4",

        # Social
        "facebook.com": "#1877F2",
        "instagram.com": "#E4405F",
        "twitter.com": "#1DA1F2",
        "x.com": "#1DA1F2",
        "reddit.com": "#FF4500",
        "linkedin.com": "#0A66C2",
        "vk.com": "#0077FF",
        "telegram.org": "#26A5E4",
        "t.me": "#26A5E4",
        "discord.com": "#5865F2",
        "whatsapp.com": "#25D366",

        # Video / media
        "youtube.com": "#FF0000",
        "twitch.tv": "#9146FF",
        "vimeo.com": "#1AB7EA",
        "spotify.com": "#1DB954",
        "soundcloud.com": "#FF5500",

        # Dev / IT
        "github.com": "#181717",
        "gitlab.com": "#FC6D26",
        "bitbucket.org": "#0052CC",
        "stackoverflow.com": "#F58025",
        "npmjs.com": "#CB3837",
        "python.org": "#3776AB",

        # Shops / services
        "amazon.com": "#FF9900",
        "ebay.com": "#E53238",
        "paypal.com": "#00457C",
        "stripe.com": "#635BFF",

        # Platforms / OS
        "windows.com": "#0078D4",
        "apple.com": "#000000",
        "android.com": "#3DDC84",
    }

        return BRAND_COLORS.get(domain, "#FFFFFF")  # Черный по умолчанию