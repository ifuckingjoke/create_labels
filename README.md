# Create Labels — v2.0.0

----------------- RU ----------------

Create Labels — это утилита для создания ярлыков сайтов с автоматически сгенерированными иконками на основе Font Awesome.

Иконки генерируются локально с использованием PIL и Font Awesome Brands, кешируются и повторно используются, чтобы ярлыки оставались стабильными между перезагрузками системы.

---

## ✨ Что нового в v2.0.0

- 🔒 Исправлено хранение иконок в exe-сборке  
  Иконки больше не сохраняются во временной директории PyInstaller (`_MEI`), которая очищается после перезагрузки.  
  Теперь кэш иконок хранится рядом с executable-файлом.

- 🎨 Улучшен рендер иконок  
  - Иконки брендов теперь отрисовываются **белым цветом** для лучшей читаемости
  - Расширен список брендовых цветов для популярных сервисов

- 🧹 Очищен словарь Font Awesome  
  Удалены несуществующие и некорректные иконки.  
  Используются **только реальные иконки из Font Awesome Brands**.

---

## 🖼 Как работают иконки

1. Для домена сайта ищется соответствующая иконка в `fa-brands`
2. Если иконка найдена — она рендерится с брендовой цветовой схемой
3. Если иконка **не найдена**, используется **дефолтная иконка Font Awesome (globe)**

> ⚠️ **Важно:**  
> Далеко не все сервисы имеют брендовые иконки в Font Awesome.  
> Это особенно касается **российских и региональных сервисов**.

---

## 🇷🇺 Поддержка российских сервисов

На данный момент **поддерживаются не все российские сервисы**.

Если для сервиса:
- нет официальной иконки в Font Awesome Brands
- или бренд отсутствует в словаре проекта

→ иконка автоматически заменяется на **стандартную иконку Font Awesome**.

Это осознанное ограничение, связанное с тем, что проект использует **только официальные брендовые иконки**, без кастомных SVG или сторонних наборов.

---

## 📁 Кэширование иконок

Сгенерированные иконки сохраняются в директорию:

_cache/

расположенную **рядом с executable-файлом** (или рядом с проектом при запуске из Python).

Это позволяет:
- избежать повторной генерации иконок
- сохранить иконки между перезагрузками
- гарантировать стабильный внешний вид ярлыков

---

## 🧩 Используемые технологии

- Python
- Pillow (PIL)
- Font Awesome Brands
- PyInstaller (для exe-сборки)

---

## 🚧 Ограничения

- Используются **только иконки Font Awesome Brands**
- Нет поддержки кастомных SVG
- Некоторые домены и сервисы будут отображаться с дефолтной иконкой

---

## 📌 Планы на будущее

- Расширение словаря брендов
- Улучшенная нормализация доменов
- Возможность кастомных иконок

---

Если вы нашли некорректный бренд, цвет или домен — pull requests и issues приветствуются.

---------------- EN --------------------------

Create Labels is a utility for generating website shortcuts with automatically rendered icons based on Font Awesome.

Icons are generated locally using Pillow and Font Awesome Brands, cached, and reused to ensure shortcut icons remain stable across system reboots.

---

## ✨ What’s new in v2.0.0

- 🔒 Fixed icon caching in PyInstaller exe builds  
  Icons are no longer stored inside the temporary PyInstaller `_MEI` directory, which gets cleaned after reboot.  
  Icon cache is now stored next to the executable file.

- 🎨 Improved icon rendering  
  - Brand icons are now rendered using **white glyphs** for better contrast  
  - Expanded brand color palette for popular services

- 🧹 Cleaned up Font Awesome mapping  
  Invalid and non-existent icons were removed.  
  Only **actual Font Awesome Brands icons** are used.

---

## 🖼 How icons work

1. The domain name is matched against the Font Awesome Brands dictionary
2. If a matching brand icon exists, it is rendered using the brand color
3. If no matching icon is found, a **default Font Awesome icon (globe)** is used instead

> ⚠️ **Important:**  
> Not all services have brand icons in Font Awesome.  
> This is especially true for **regional and Russian services**.

---

## 🇷🇺 Russian services support

At the moment, **not all Russian services are supported**.

If a service:
- does not have an official Font Awesome brand icon
- or is missing from the project’s brand dictionary

→ the icon will automatically fall back to the **default Font Awesome icon**.

This is an intentional limitation, as the project relies strictly on **official Font Awesome Brands icons**, without custom SVGs or third-party icon packs.

---

## 📁 Icon caching

Generated icons are stored in the following directory:

_cache/


located **next to the executable file** (or next to the project directory when running from Python).

This allows:
- avoiding unnecessary icon regeneration
- preserving icons across reboots
- ensuring consistent shortcut appearance

---

## 🧩 Tech stack

- Python
- Pillow (PIL)
- Font Awesome Brands
- PyInstaller (for exe builds)

---

## 🚧 Limitations

- Only Font Awesome Brands icons are supported
- No custom SVG icons
- Some services will always fall back to the default icon

---

## 📌 Roadmap

- Expanded brand dictionary
- Improved domain normalization
- Optional custom icon support

---

If you encounter an incorrect brand, color, or domain mapping — issues and pull requests are welcome.
