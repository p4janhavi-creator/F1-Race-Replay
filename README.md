# 🏎️ F1 Race Replay

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastF1](https://img.shields.io/badge/Data-FastF1-red)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

> A Python-based Formula 1 race replay simulator that visualizes real F1 telemetry and timing data. Watch every driver move around the circuit in real time while tracking positions, tyre compounds, and race progression through a live leaderboard.

---

# 🏁 Project Highlights

- 🏎️ Real Formula 1 Telemetry Visualization
- 📡 FastF1 API Integration
- 🗺️ Live Track Mapping
- 🎞️ Real-Time Replay Engine
- 📋 Dynamic Leaderboard
- 🛞 Tyre Compound Tracking
- ⏱️ Session Time Synchronization
- ⌨️ Interactive Replay Controls

---

# 🎯 Why This Project?

Formula 1 generates enormous amounts of telemetry and timing data during every session.

This project transforms raw race data into an interactive replay experience, allowing users to:

- Visualize driver movement around the circuit
- Analyze race progression in real time
- Track driver positions throughout a session
- Monitor tyre strategies and race dynamics
- Explore Formula 1 telemetry in a visual and intuitive way

---

# 🧩 Project Overview

```mermaid
mindmap
  root((F1 Race Replay))
    Data Collection
      FastF1 API
      Telemetry Data
      Timing Data
      Session Data
    Processing
      Driver Coordinates
      Lap Information
      Track Mapping
    Replay Engine
      Position Updates
      Frame Generation
      Time Synchronization
    Visualization
      Track Map
      Driver Markers
      Leaderboard
      Tyre Data
    Controls
      Pause
      Rewind
      Fast Forward
```

---

# 🏗️ System Architecture

```mermaid
flowchart TD

    U[👤 User]

    U --> M[🏁 Session Selection]

    M --> F[📡 FastF1 Data Fetcher]

    F --> P[📊 Telemetry Processor]

    P --> T[🗺️ Track Coordinate Mapper]

    T --> R[🎞️ Replay Engine]

    R --> V[📈 Visualization Layer]

    V --> L[📋 Live Leaderboard]

    V --> D[🏎️ Driver Position Renderer]

    L --> U
    D --> U
```

---

# 🔄 Replay Workflow

```mermaid
sequenceDiagram

    participant User
    participant FastF1
    participant Processor
    participant Replay
    participant Display

    User->>FastF1: Select Session

    FastF1->>Processor: Load Telemetry Data

    Processor->>Processor: Extract Driver Coordinates

    Processor->>Replay: Generate Replay Frames

    Replay->>Display: Update Driver Positions

    Replay->>Display: Update Leaderboard

    Display-->>User: Render Replay
```

---

# 🧠 Replay Engine Pipeline

```mermaid
flowchart LR

A[Session Selection]
--> B[Fetch Telemetry]

B --> C[Extract Coordinates]

C --> D[Calculate Driver Positions]

D --> E[Generate Animation Frames]

E --> F[Update Leaderboard]

F --> G[Render Replay]
```

---

# ✨ Features

### 🗺️ Animated Track Map

Displays all drivers moving simultaneously around the circuit using team colours.

### 📋 Live Leaderboard

Updates race positions and tyre compounds in real time.

### ⏱️ Session Timer

Shows elapsed race or qualifying session time.

### ⌨️ Interactive Replay Controls

Pause, rewind, and fast-forward the replay.

### 🏁 Multi-Session Support

Supports:

- Race Sessions
- Qualifying Sessions
- Sprint Sessions
- Practice Sessions

---

# 🎮 Controls

| Key | Action |
|------|----------|
| Space | Pause / Resume |
| → Right Arrow | Skip Forward |
| ← Left Arrow | Skip Backward |

---

# 🖥️ Demo

Add screenshots or a GIF here.

```markdown




```

Or:

```markdown
![Replay Screenshot](screenshot.png)
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/p4janhavi-creator/F1-Race-Replay.git
cd F1-Race-Replay
```

## Install Dependencies

```bash
pip install fastf1 matplotlib
```

## Run Application

```bash
python main.py
```

---

# 🚀 Usage

When the application starts:

```text
========================================
          F1 RACE REPLAY
========================================

Enter year (e.g. 2023): 2023
Enter race name (e.g. Monaco): Monaco
Enter session (R = Race, Q = Qualifying): R
```

The replay window will open automatically and begin animating the selected session.

---

# 📂 Project Structure

```text
F1-Race-Replay
│
├── main.py         # Main application entry point
├── replay.py       # Replay engine
├── track.py        # Track visualization
├── fetch_data.py   # Telemetry data fetching
├── menu.py         # User input interface
├── cache/          # FastF1 cached session data
└── README.md
```

---

# 🔧 Dependencies

### FastF1

Provides official Formula 1 telemetry and timing data.

### Matplotlib

Used for track rendering, animation, and leaderboard visualization.

---

# 📚 Learning Outcomes

This project demonstrates:

- Python Application Development
- Data Visualization
- Sports Analytics
- Telemetry Processing
- API Integration
- Real-Time Animation
- Simulation Systems
- Event-Driven Programming

---

# 🚀 Future Enhancements

- 📊 Lap Time Analytics Dashboard
- 🛞 Pit Stop Visualization
- 📈 Sector Time Comparisons
- 🏎️ Driver Battle Detection
- 🎥 Export Replay as Video
- 🌐 Interactive Web Version
- 🤖 AI-Powered Race Insights

---

# 👩‍💻 Author

**Janhavi Patil**

BE Artificial Intelligence & Data Science

Passionate about AI, Data Analytics, Motorsport Technology, and Building Interactive Software Systems.

---

# ⭐ Support

If you enjoyed this project, consider giving it a ⭐ on GitHub!

It helps others discover the project and motivates future improvements. 🏎️💨
