
# 🧠 Map Confidence Spectrum (Wolves POV CLI Tool)

This is a simple CLI tool that helps Valorant analysts visualize **map matchup confidence** between their team and an upcoming opponent — from their team's point of view.

It outputs a **7-box color spectrum** showing which maps are weak (red), neutral (white), and strong (green) for your team based on the upcoming opponent.

This forked version is for analyzing Kings Ascend Season 2.

Original code from Ominous from Wolves Esports. Below are the original README description.
---

## 📦 Requirements

- Python 3.x
- pandas
- matplotlib

Install requirements:

```bash
pip install pandas matplotlib
```

---

## 🚀 Usage

```bash
python3 spectrum_cli.py --wolves your_team.csv --opponent opponent_team.csv [--output filename.png]
```

### ✅ Example (Wolves vs DRG)

```bash
python3 spectrum_cli.py --wolves wolves.csv --opponent drg.csv --output spectrum_drg.png
```

---

## 📁 CSV Format

Each team’s CSV should look like this:

| Map      | Picks | Bans | Wins | Losses |
|----------|-------|------|------|--------|
| Pearl    | 3     | 1    | 3    | 0      |
| Haven    | 2     | 0    | 2    | 0      |
| Icebox   | 2     | 1    | 1    | 1      |
| Split    | 0     | 2    | 0    | 0      |
| Fracture | 1     | 2    | 0    | 1      |
| Lotus    | 2     | 0    | 2    | 0      |
| Ascent   | 1     | 3    | 0    | 1      |

- Map names must match exactly: Pearl, Haven, Icebox, Split, Fracture, Lotus, Ascent
- Win rate, picks, and bans are used to calculate the confidence score

---

## 🎨 Output

A horizontal bar showing 7 maps:
- Red = low confidence
- White = even/neutral
- Green = high confidence

Output is saved as a `.png` file (default: `map_confidence_spectrum.png`)

---

## 🤝 Reusable for Any Team

Just set `--wolves` to your own team file. The confidence spectrum will always reflect your POV.
