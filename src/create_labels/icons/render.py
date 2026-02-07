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
        brand_colors = {
            "youtube.com": "#FF0000",      # YouTube red
            "github.com": "#181717",        # GitHub black
            "google.com": "#4285F4",        # Google blue
            "vk.com": "#0077FF",            # VK blue
            "telegram.org": "#26A5E4",      # Telegram light blue
            "x.com": "#1DA1F2",       # Twitter blue
            "facebook.com": "#1877F2",      # Facebook blue
            "instagram.com": "#E4405F",     # Instagram pink
            "whatsapp.com": "#25D366",      # WhatsApp green
            "discord.com": "#5865F2",       # Discord blurple
            "reddit.com": "#FF4500",        # Reddit orange
            "spotify.com": "#1DB954",       # Spotify green
            "twitch.tv": "#9146FF",         # Twitch purple
            "tiktok.com": "#000000",        # TikTok black
            "linkedin.com": "#0A66C2",      # LinkedIn blue
        }
        return brand_colors.get(domain, "#000000")  # Черный по умолчанию