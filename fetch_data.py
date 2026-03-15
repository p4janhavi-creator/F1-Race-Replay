import fastf1

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2023, "Monaco", "R")
session.load()

laps = session.laps

# See all the column names available to us
print("=== COLUMNS ===")
print(laps.columns.tolist())

# Look at one driver — Verstappen
print("\n=== VERSTAPPEN'S LAPS ===")
ver_laps = laps[laps["Driver"] == "VER"]
print(ver_laps[["LapNumber", "LapTime", "Compound", "PitInTime", "PitOutTime"]].to_string())

# See all drivers in the race
print("\n=== ALL DRIVERS ===")
print(laps["Driver"].unique())