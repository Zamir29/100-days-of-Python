from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import (
    BILLBOARD_LISTS_URL,
    BILLBOARD_URL,
    THIS_YEAR,
    USER_AGENT,
    SPOTIFY_URI,
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET
)

def check_date(input_date, wiki_available_date):
    while True:
        try:
            # Split string by -
            checking_date = input_date.split("-")

            # Check if there are three items
            if len(checking_date) != 3:
                raise ValueError("Format is not valid!")

            # Check if the numbers are not letters
            for num in checking_date:
                if not num.isdigit():
                    raise ValueError(f"'{num}' is not a number!")

            # Map every item as an int
            year, month, day = map(int, checking_date)

            try:
                # Check if date is a calendar valid date
                datetime(year=year, month=month, day=day)


            except ValueError:
                    raise ValueError("The date you entered does not exist!")

            # Check if year is within the range
            start_year, last_year = wiki_available_date

            if not (start_year <= year <= THIS_YEAR):
                raise ValueError(f"Please enter a year between {start_year} and {THIS_YEAR}.")

            if year > last_year:
                if year == THIS_YEAR:
                    raise ValueError(f"The billboard for {year} is not available yet! The last available is {last_year}.")
                else:
                    raise ValueError(f"Billboard data is only available up to {last_year}.")

            return year

        except ValueError as error:
            print(error)
            input_date = input("Please enter a year in the format YYYY-MM-DD: ")

def wiki_date_available():
    # Get the response from wiki and build the soup
    headers = {
        "User-Agent": USER_AGENT,
    }
    response = requests.get(url=BILLBOARD_LISTS_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Target the div that contains all the anchors to the billboards
    groups = soup.find_all("div", class_="mw-category-group")
    years = []

    for group in groups:
        for a in group.find_all("a"):
            title = a.get("title", "")
            parts = title.split()
            if parts and parts[-1].isdigit():
                years.append(int(parts[-1]))

    # Extract the starting year and the last year available
    start_year = min(years)
    last_year = max(years)

    return start_year, last_year

def wiki_billboard(year):
    # Get the response from wiki and build the soup
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15"
    }

    response = requests.get(url=f'{BILLBOARD_URL}{year}', headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find(name="table", class_="wikitable sortable")
    body_rows = table.find_all(name="tr")[1:]

    songs = []
    for row in body_rows:
        cells = row.find_all(name="td")
        if len(cells) < 3:
            continue

        # Get the rank
        rank = cells[0].get_text(strip=True)

        # Get title inside the <a>, no surrounding quotes
        title_tag = cells[1].select_one("a")
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            title = cells[1].get_text(strip=True)

        # Get artists spaced and without the \n at the end
        artist_tag = cells[2].select_one("a")
        if artist_tag:
            artist = artist_tag.get_text(strip=True)
        else:
            artist = cells[2].get_text(strip=True)

        song_data = {
            "no.": rank,
            "title": title,
            "artist": artist,
        }
        songs.append(song_data)

    return songs

def get_spotify_client(scope: str):
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=f"{SPOTIFY_CLIENT_ID}",
            client_secret=f"{SPOTIFY_CLIENT_SECRET}",
            redirect_uri=f"{SPOTIFY_URI}",
            scope=scope))

def get_spotify_uri(sp_client, track: dict[str, str]):
    q = f"track:{track['title']} artist:{track['artist']}"

    search_track = sp_client.search(
        q=q,
        limit=1,
        type="track")

    track_uri = search_track["tracks"]["items"]

    if not track_uri:
        print(f"No track found for {track['title']}")
        return None

    return track_uri[0]["uri"]

def find_playlist_by_name(sp_client, playlist_name: str, user_id: str):
    results = sp_client.user_playlists(
        user=user_id,
        limit=50,
    )

    while results:
        for playlist in results["items"]:
            if playlist["name"] == playlist_name:
                return playlist
        results = sp_client.next(results) if results["next"] else None

    return None

def main():
    # Get available years of Billboards on wiki
    available_years = wiki_date_available()
    # Get the year from the user
    ask_date = input("What year would you like to travel? 🚋\nType in this format YYYY-MM-DD: ")

    # Checking the date
    scraping_date = check_date(ask_date, available_years)
    print(f"📝\nUsing scraping year: {scraping_date}\n")

    billboard_list = wiki_billboard(scraping_date)

    # Spotify auth test
    sp = get_spotify_client("playlist-modify-private")
    user_id = sp.me()["id"]
    print("⌛️ Now searching all the tracks URI...\n")

    # Build the list of URIS to post
    track_uris_list = []
    for track in billboard_list:
        track_uri = get_spotify_uri(sp, track)
        if not track_uri:
            continue
        track_uris_list.append(track_uri)

    # Prepare the playlist name and check if there is already an existing one to use it id
    playlist_name = f"{scraping_date} - Year-End Hot 100 singles"
    print(f"⌛️ Now creating the playlist '{playlist_name}' and adding tracks...\n")

    # Check if a playlist exists and use that id instead
    existing = find_playlist_by_name(sp, playlist_name, user_id)
    if existing:
        playlist_id = existing["id"]
        print(f"✅ Using existing Playlist: '{playlist_name}'\n")
    else:
        create_playlist = sp.user_playlist_create(
            user=user_id,
            name=playlist_name,
            public=False,
            description=f"Billboard Year-End Hot 100 singles of {scraping_date}"
        )

        playlist_id = create_playlist["id"]
        print(f"🆕 Created playlist: {playlist_name}")

    # Add all the tracks using the list of URI on the playlist
    add_items = sp.playlist_add_items(
        playlist_id=playlist_id,
        items=track_uris_list,
    )

    # Check if everything is OK
    if add_items:
        print(f"All the items added to playlist: {playlist_name}")
    else:
        print("Uhm.. something went wrong!")

if __name__ == '__main__':
    main()
