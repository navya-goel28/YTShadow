print("🚀 Script started")

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import re

# Scope for YouTube read/write
SCOPES = ["https://www.googleapis.com/auth/youtube"]

def authenticate_youtube():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    credentials = flow.run_local_server(port=8080)
    return build("youtube", "v3", credentials=credentials)

def extract_playlist_id(url):
    match = re.search(r"(?:list=)([a-zA-Z0-9_-]+)", url)
    return match.group(1) if match else None

def get_videos_from_playlist(youtube, playlist_id):
    videos = []
    next_page_token = None
    while True:
        pl_request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        pl_response = pl_request.execute()

        for item in pl_response["items"]:
            videos.append(item["contentDetails"]["videoId"])

        next_page_token = pl_response.get("nextPageToken")
        if not next_page_token:
            break
    return videos

def create_new_playlist(youtube, title, description=""):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()
    return response["id"]

def add_videos_to_playlist(youtube, playlist_id, video_ids):
    for vid in video_ids:
        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": vid
                    }
                }
            }
        ).execute()

def main():
    youtube = authenticate_youtube()
    playlist_url = input("Enter the public playlist URL: ").strip()
    new_title = input("Enter a title for your private copy: ").strip()

    playlist_id = extract_playlist_id(playlist_url)
    if not playlist_id:
        print("Invalid playlist URL.")
        return

    print("Fetching videos...")
    videos = get_videos_from_playlist(youtube, playlist_id)
    print(f"Found {len(videos)} videos.")

    print("Creating new playlist...")
    new_playlist_id = create_new_playlist(youtube, new_title, "Copied from another playlist")

    print("Adding videos...")
    add_videos_to_playlist(youtube, new_playlist_id, videos)

    print("✅ Playlist copied successfully and set to private!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        print("❌ ERROR:", e)
        traceback.print_exc()
