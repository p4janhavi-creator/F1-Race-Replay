import fastf1

fastf1.Cache.enable_cache("cache")

print("=" * 40)
print("       F1 RACE REPLAY")
print("=" * 40)

# Ask user for input
year = int(input("\nEnter year (e.g. 2023): "))
track = input("Enter race name (e.g. Monaco): ")
session_type = input("Enter session type (R = Race, Q = Qualifying): ")

print(f"\nLoading {year} {track} {session_type}...")

# Load the session with user's choices
session = fastf1.get_session(year, track, session_type)
session.load()

print(f"\nLoaded! Drivers in this session:")
print(session.drivers)