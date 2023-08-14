import requests
import json

# Set the access token and API endpoint URLs
access_token = "BQD8XDthjAtEZfedjMPydpgGjsnUyOkXj_7I5fUymaGHs2vRYX_84J50MKB07e6O9B5UbSV63E20AqjykBASvY6aSECR0aOijRT00ONpuFud_sfPdUOLcugdUXeQvChF4WVCDAKb_udXqQNtCLNZZ34p92qkNTpADYjZkRApJRePmfmqan6nD_U_Af9dNN3Jb_ZsoREMnI5mgtWXGhajMjEC2160gOKFVlc8MOQE3PYX1MLDfd1OMNhrHvXwNyABRD4XS8CX-eQL7X3OzVe_X6sVOcfq-l0ctH7Y1MPq1NvjNf5C5LmjIzWew1FKk4KV7f8SPxCs-8OVD5citA1kXB9pkA"
now_playing_url = "https://api.spotify.com/v1/me/player/currently-playing"
like_track_url = "https://api.spotify.com/v1/me/tracks"

# Define the headers for the requests
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Send a GET request to retrieve the currently playing track
response = requests.get(now_playing_url, headers=headers)
requests.get(now_playing_url, headers=headers)
# Check if the response contains a currently playing track
if response.status_code == 200 and "item" in response.json():

    # Get the ID of the currently playing track
    track_id = response.json()["item"]["id"]

    # Send a PUT request to "like" the currently playing track
    like_payload = json.dumps({"ids": [track_id]})
    like_response = requests.put(like_track_url, headers=headers, data=like_payload)

    # Check if the track was successfully liked
    if like_response.status_code == 200:
        print("Liked the currently playing track!")
    else:
        print("Failed to like the currently playing track.")
else:
    print("No track is currently playing.")
    print(response.status_code)
    print(response)
