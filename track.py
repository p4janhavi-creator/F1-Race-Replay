import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2023, "Monaco", "R")
session.load()

# Get Verstappen's position data
ver_pos = session.pos_data["1"]

# Create a figure (the window) and axes (the drawing area)
fig, ax = plt.subplots(figsize=(10, 8))

# Plot every X,Y position VER was at during the race
# This traces the shape of the circuit!
ax.plot(ver_pos["X"], ver_pos["Y"], color="gray", linewidth=1, label="Track")

# Now let's place a dot showing where VER was at the very start
start = ver_pos.iloc[0]  # iloc[0] means "give me row number 0" (the first row)
ax.plot(start["X"], start["Y"], "ro", markersize=10, label="VER start position")

# Labels and title
ax.set_title("Monaco Grand Prix 2023 - Track Map")
ax.set_aspect("equal")  # makes sure the track isn't stretched or squished
ax.legend()

# Show the window
plt.show()