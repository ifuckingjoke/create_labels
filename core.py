from urllib.parse import urlparse
from titles import WebTitles
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from create_labels.icons import get_ico # type: ignore


class Shortcut:

    APP_NAME = "CreateLabels"

    @staticmethod
    def shortcut_api(path: str, url: str):
        title = Shortcut.get_title(url)
        domain = Shortcut.get_domain(url)
        
        icon_path = get_ico(domain)

        number = 1
        orig_path = path

        while os.path.exists(path):
            path = orig_path.replace('.url', f' ({number}).url')
            number += 1
            if number > 999:
                break

        with open(path, "w", encoding="utf-8") as f:
            f.write("[InternetShortcut]\n")
            f.write(f"URL={url}\n")

            if icon_path:
                f.write(f"IconFile={icon_path}\n")
                f.write("IconIndex=0\n")
        
        return path
    
    @staticmethod
    def get_title(url):

        domain = Shortcut.get_domain(url)
        
        titles = WebTitles.titles.get(domain)

        if not titles:
            titles = "WebSite"
        
        return titles
    
    @staticmethod
    def get_domain(url: str) -> str:
        
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        return domain

