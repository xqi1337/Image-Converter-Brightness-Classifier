# Image Converter & Brightness Classifier

Dieses Python-Skript konvertiert alle `.jpg` und `.jpeg` Bilder in einem Verzeichnis zu `.png` und klassifiziert sie anschließend automatisch in helle und dunkle Bilder basierend auf Helligkeit und Weißanteil.

## 🔧 Features

- ✅ Konvertiert `.jpg` und `.jpeg` Bilder zu `.png`
- ✅ Helligkeitsanalyse durch Durchschnittslichtwert und Weißanteil
- ✅ Sortiert Bilder in `bright/` und `dark/` Unterordner
- ✅ Nutzt OpenCV und Pillow für Bildverarbeitung
- ✅ Saubere Konsolenausgabe zur Nachverfolgung

## 📁 Struktur

Nach Ausführung:
```
project-folder/
├── bright/
│   └── image1.png
├── dark/
│   └── image2.png
├── original_images.jpg/png
├── jpg_into_png.py
├── image_sorter_bright_dark.py
└── README.md
```

## ▶️ Verwendung

1. **Installiere Abhängigkeiten** (am besten in einer virtuellen Umgebung):

```bash
pip install pillow opencv-python numpy
```

2. **Speichere das Skript als z. B. `main.py`** und führe es aus:

```bash
python image_sorter_bright_dark.py
python jpg_into_png.py
```

Das Skript konvertiert alle `.jpg/.jpeg` Bilder im aktuellen Verzeichnis zu `.png` und sortiert die `.png`-Dateien in `bright/` oder `dark/` Verzeichnisse.

## 💡 Wie funktioniert die Klassifizierung?

Die Funktion `isbright()`:

- verkleinert das Bild für Effizienz,
- wandelt es in LAB-Farbraum um,
- analysiert die **Luminanz (Helligkeit)**,
- zählt helle Pixel (über 95 % Helligkeit),
- und entscheidet auf Basis von Mittelwert + Weißanteil.

## 📸 Beispielausgabe

```
Converted 'photo1.jpg' to 'photo1.png'
photo1.png moved to bright
photo2.png moved to dark
Finished!

2 images classified as bright.
1 image classified as dark.
```

## 🛠️ Konfigurierbare Parameter

- `thresh_mean`: Schwelle für mittlere Helligkeit (Standard: 0.5)
- `thresh_white`: Weißpixel-Anteil (Standard: 0.4)
- `dim`: Bildverkleinerung für Performance (Standard: 10x10)

Du kannst diese Werte in der Funktion `isbright()` anpassen.

## 📜 Lizenz

MIT License – freie Nutzung erlaubt, aber bitte mit Verweis auf dieses Repository.
