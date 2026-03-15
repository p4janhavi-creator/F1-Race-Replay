import fastf1
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fastf1.Cache.enable_cache("cache")

# =====================
# MENU
# =====================
def show_menu():
    print("=" * 40)
    print("       F1 RACE REPLAY")
    print("=" * 40)
    
    year = int(input("\nEnter year (e.g. 2023): "))
    track = input("Enter race name (e.g. Monaco): ")
    session_type = input("Enter session (R = Race, Q = Qualifying): ")
    
    return year, track, session_type

# =====================
# REPLAY
# =====================
def start_replay(year, track, session_type):
    print(f"\nLoading {year} {track} {session_type}...")
    
    session = fastf1.get_session(year, track, session_type)
    session.load()

    # Load all drivers
    all_drivers = {}
    for driver_number in session.drivers:
        try:
            all_drivers[driver_number] = session.pos_data[driver_number]
        except:
            pass

    # Team colors
    team_colors = {
        "VER": "blue", "PER": "blue",
        "HAM": "cyan", "RUS": "cyan",
        "LEC": "red", "SAI": "red",
        "NOR": "orange", "PIA": "orange",
        "ALO": "green", "STR": "green",
        "GAS": "pink", "OCO": "pink",
        "ALB": "white", "SAR": "white",
        "TSU": "purple", "DEV": "purple",
        "HUL": "gray", "MAG": "gray",
        "BOT": "lime", "ZHO": "lime",
    }

    # Tyre compound short names
    compound_colors = {
        "SOFT": ("S", "red"),
        "MEDIUM": ("M", "yellow"),
        "HARD": ("H", "white"),
        "INTERMEDIATE": ("I", "green"),
        "WET": ("W", "blue"),
    }

    # Map driver numbers to abbreviations
    driver_map = {}
    for driver_number in all_drivers:
        abbr = session.get_driver(driver_number)["Abbreviation"]
        driver_map[driver_number] = abbr

    # Draw the track
    fig, (ax, ax_lb) = plt.subplots(1, 2, figsize=(20, 10),
                                      gridspec_kw={"width_ratios": [2, 1]})
    fig.patch.set_facecolor("black")

    # Track area
    ax.set_facecolor("black")
    first_driver = list(all_drivers.keys())[0]
    track_pos = all_drivers[first_driver]
    ax.plot(track_pos["X"], track_pos["Y"], color="gray", linewidth=2, zorder=0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"{track} {year} - {session_type}", color="white", fontsize=16)

    # Leaderboard area
    ax_lb.set_facecolor("black")
    ax_lb.axis("off")
    ax_lb.set_title("LEADERBOARD", color="white", fontsize=14, fontweight="bold")

    # Create dots and labels
    dots = {}
    labels = {}
    for driver_number, abbr in driver_map.items():
        color = team_colors.get(abbr, "white")
        dot, = ax.plot([], [], "o", color=color, markersize=8, zorder=5)
        dots[driver_number] = dot
        label = ax.text(0, 0, abbr, color=color, fontsize=6,
                        fontweight="bold", zorder=6, visible=False)
        labels[driver_number] = label

    # Time display
    time_display = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                           color="white", fontsize=12, verticalalignment="top")

    # Leaderboard rows
    leaderboard_rows = []
    for i in range(20):
        row_text = ax_lb.text(
            0.05, 0.95 - (i * 0.047), "",
            transform=ax_lb.transAxes,
            color="white", fontsize=11,
            fontfamily="monospace"
        )
        leaderboard_rows.append(row_text)

    all_laps = session.laps
    is_paused = [False]
    frame_index = [0]

    def on_keypress(event):
        if event.key == " ":
            is_paused[0] = not is_paused[0]
        if event.key == "right":
            frame_index[0] += 500
        if event.key == "left":
            frame_index[0] = max(0, frame_index[0] - 500)

    fig.canvas.mpl_connect("key_press_event", on_keypress)

    def get_leaderboard(current_time):
        standings = []
        for driver_number, abbr in driver_map.items():
            driver_laps = all_laps[
                (all_laps["DriverNumber"] == driver_number) &
                (all_laps["Time"] <= current_time)
            ]
            if len(driver_laps) > 0:
                latest_lap = driver_laps.iloc[-1]
                position = latest_lap["Position"]
                compound = latest_lap["Compound"]
            else:
                position = 99
                compound = "?"
            standings.append((position, abbr, compound))
        standings.sort(key=lambda x: x[0])
        return standings

    def update(frame):
        if is_paused[0]:
            return list(dots.values()) + list(labels.values()) + [time_display] + leaderboard_rows

        i = frame_index[0]
        frame_index[0] += 2
        current_time = None

        for driver_number, dot in dots.items():
            pos = all_drivers[driver_number]
            if i < len(pos):
                row = pos.iloc[i]
                x, y = row["X"], row["Y"]
                dot.set_data([x], [y])
                labels[driver_number].set_position((x + 15, y + 15))
                labels[driver_number].set_visible(True)

                if driver_number == list(all_drivers.keys())[0]:
                    current_time = row["SessionTime"]
                    t = row["SessionTime"]
                    total_seconds = int(t.total_seconds())
                    minutes = total_seconds // 60
                    seconds = total_seconds % 60
                    time_display.set_text(f"Time: {minutes:02d}:{seconds:02d}")

        if current_time is not None:
            standings = get_leaderboard(current_time)
            for idx, (position, abbr, compound) in enumerate(standings):
                compound_short, compound_color = compound_colors.get(compound, ("?", "white"))
                leaderboard_rows[idx].set_text(
                    f"P{int(position):02d}  {abbr}  [{compound_short}]"
                )
                color = team_colors.get(abbr, "white")
                leaderboard_rows[idx].set_color(color)

        return list(dots.values()) + list(labels.values()) + [time_display] + leaderboard_rows

    ani = animation.FuncAnimation(fig, update, frames=20000, interval=20, blit=True)
    plt.show()

# =====================
# RUN THE APP
# =====================
year, track, session_type = show_menu()
start_replay(year, track, session_type)