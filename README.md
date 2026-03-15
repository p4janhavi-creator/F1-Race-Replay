# 🏎️ F1 Race Replay

A Python app that animates real F1 race and qualifying sessions using live telemetry data. Watch all drivers move around the circuit in real time, with a live leaderboard showing positions and tyre compounds.

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![FastF1](https://img.shields.io/badge/FastF1-latest-red)

---

## Features

- 🗺️ **Animated track map** — all drivers plotted simultaneously with team colours
- 📋 **Live leaderboard** — updates in real time with position and tyre compound
- ⏱️ **Session timer** — shows elapsed race/qualifying time
- ⌨️ **Keyboard controls** — pause, rewind and fast-forward the replay
- 🏁 **Any session** — works for Race, Qualifying, and more

---

## Controls

| Key | Action |
|-----|--------|
| `Space` | Pause / Resume |
| `→` Right Arrow | Skip forward |
| `←` Left Arrow | Skip backward |

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/f1-race-replay.git
cd f1-race-replay
```

### 2. Install dependencies
```bash
pip install fastf1 matplotlib
```

### 3. Run the app
```bash
python main.py
```

---

## Usage

When you run the app, you'll be prompted to enter:

```
========================================
       F1 RACE REPLAY
========================================

Enter year (e.g. 2023): 2023
Enter race name (e.g. Monaco): Monaco
Enter session (R = Race, Q = Qualifying): R
```

The replay window will open and start animating automatically.

---

## Project Structure

```
f1-race-replay/
├── main.py        # Entry point — menu + replay logic
├── replay.py      # Standalone replay script (Monaco 2023)
├── track.py       # Simple track map visualiser
├── fetch_data.py  # Data exploration / testing script
├── menu.py        # Standalone menu script
└── .gitignore
```

---

## Dependencies

- [FastF1](https://docs.fastf1.dev/) — F1 telemetry and timing data
- [Matplotlib](https://matplotlib.org/) — Visualisation and animation

---

## Notes

- FastF1 caches session data in a `cache/` folder on first load — subsequent runs are much faster
- Data is sourced from the official F1 timing feed via FastF1
