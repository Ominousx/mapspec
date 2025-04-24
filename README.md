## 🇬🇧 MapSpec – Veto Prep Tool for Valorant (with JP support)

MapSpec is a pre-match **map confidence spectrum generator** for Valorant. It helps analysts make smart **pick/ban decisions** by comparing historical map performance between two teams.

You can run it via:
- ✅ Python CLI (local use)
- ✅ Google Colab (with Japanese support via `japanize-matplotlib`)

---

## 📊 Example: Confidence Spectrum
<img src="spectrum_example.png" width="600" />

---

## 👤 Authors

| Name | GitHub | Role |
|------|--------|------|
| **Sushant Jha** | [@Ominousx](https://github.com/Ominousx) | 🧠 Project Lead / CLI Developer |
| **nolozy** | [@nolozy](https://github.com/nolozy) | 🇪・ Colab Notebook + 🇯🇵 Localization |

---

## 🛠️ Installation (Local CLI)

```bash
git clone https://github.com/Ominousx/mapspec.git
cd mapspec
pip install -r requirements.txt
```

Then run:

```bash
python3 spectrum_cli.py --wolves wolves.csv --opponent geng.csv --output spectrum.png
```

---

## ☁️ Google Colab (JP-ready)

If you're using Google Colab:

1. Create this folder structure in Google Drive:
```
/My Drive
└── Colab Notebooks
    └── mapspec
        ├── wolves.csv
        └── teams/
            └── blg/
                └── blg.csv
```

2. Open `mapspec_colab.ipynb` from [@nolozy’s fork](https://github.com/nolozy/mapspec)

3. Run the notebook to generate spectrum chart with **Japanese labels**.

---

## 🌐 Language Support

| Language | Interface | Notes |
|----------|-----------|-------|
| English  | ✅ CLI + README | Default |
| Japanese | ✅ Colab notebook (`japanize-matplotlib`) | Developed by [@nolozy](https://github.com/nolozy) |
