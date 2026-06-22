# 🎵 Spotify Organiser

A Python tool that generates randomised Spotify playlists by pulling tracks from a curated collection of artist playlists and shuffling them into a fresh mix — automatically created and saved to your Spotify account.

## How It Works

1. **Reads** a set of source playlists (one per artist/band) defined in `band_info.json`
2. **Collects** every track ID from those playlists via the Spotify API
3. **Randomly picks 40 tracks** from the pool (without duplicates)
4. **Creates a new playlist** on your Spotify account, timestamped with the current date and time

### Modes

| Script | Behaviour |
|---|---|
| `main.py` | Uses **all** playlists in `band_info.json` |
| `main-fungus_station.py` | Filters to a specific `target_playlists` subset (curated indie/alt-rock mix) |

## Artists Included

Two Door Cinema Club · Wallows · The Wombats · Cage the Elephant · Bloc Party · AJR · The Vaccines · Weezer · Foster the People · Sundara Karma · The View · alt-J · The Strokes · Glass Animals · Wet Leg · Blossoms

## Setup

### Prerequisites

- Python 3.7+
- A [Spotify Developer](https://developer.spotify.com/dashboard) application (for API credentials)

### Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/SPOTIFYORGANISER.git
cd SPOTIFYORGANISER

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and fill in your Spotify API credentials:
   ```
   client_id=YOUR_CLIENT_ID
   client_secret=YOUR_CLIENT_SECRET
   redirect_uri=http://localhost:8888/callback
   ```

> [!NOTE]
> On first run you'll be redirected to a Spotify login page in your browser to authorise the app. The resulting token is cached locally so you only need to do this once.

## Usage

```bash
# Generate a playlist using all source playlists
python main.py

# Generate a playlist using the curated subset
python main-fungus_station.py
```

A new playlist named with today's date and time (e.g. `22/06/2026  19-28`) will appear in your Spotify library.

## Project Structure

```
SPOTIFYORGANISER/
├── main.py                  # Full-catalogue playlist generator
├── main-fungus_station.py   # Filtered subset playlist generator
├── band_info.json           # Artist name → Spotify playlist URL mapping
├── requirements.txt         # Python dependencies
├── .env.example             # Template for API credentials
└── .gitignore               # Ignores secrets, caches, and venv
```

## Dependencies

- [spotipy](https://spotipy.readthedocs.io/) — Spotify Web API wrapper
- [python-dotenv](https://pypi.org/project/python-dotenv/) — `.env` file loading
- [requests](https://docs.python-requests.org/) — HTTP library

## License

This project is provided as-is for personal use.
