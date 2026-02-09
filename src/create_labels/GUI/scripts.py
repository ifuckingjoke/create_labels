import tkinter as tk
from tkinter import messagebox
import os, sys
from urllib.parse import urlparse
from core import Shortcut
import ctypes
from ctypes import wintypes


class AppFunctions:

    PLACEHOLDER = "Вставьте URL-адрес страницы из интернета"
    

    @staticmethod
    def focus_in(content, event):
        if content.entry.get() == AppFunctions.PLACEHOLDER:
            content.entry.delete(0, tk.END)
            content.entry.configure(show="")
    @staticmethod
    def focus_out(content, event):
        if content.entry.get() == "":
            content.entry.insert(0, AppFunctions.PLACEHOLDER)
            content.entry.configure(show="")
    
    @staticmethod
    def resource_path(rel):
        base = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
        return os.path.join(base, rel)

    @staticmethod
    def on_create(content):

        url = content.entry.get().strip()

        if not url or url == AppFunctions.PLACEHOLDER:
            messagebox.showwarning("Предупреждение", "Невозможно создать ярлык без URL-адреса")
            return None
        
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        
        buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(
            None, 0x10, None, 0, buf
        )
    
        desktop = buf.value

        title = Shortcut.get_title(url)
        path = os.path.join(desktop, f"{title}.url")

        try:
            Shortcut.shortcut_api(path, url)
            messagebox.showinfo("Готово", "Ярлык успешно создан")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))