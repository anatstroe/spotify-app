# import libraries
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def tokenforAna():
    client_id  = "f2302aec11b14196af5a016b6d97560e"
    client_secret = "d3ace6e041614054be1de563d3de87eb"
    return authtoken(client_id, client_secret)

def authtoken(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(auth_url, data=payload, headers=headers)
    return response.json()['access_token']   

# compose the api url
def apiurl (endpoint, api_url = "https://api.spotify.com/"):
    return f"{api_url}{endpoint}"

# Get the top artists for the user endpoint
def topArtistsEndpoint (time_range, limit):
    return f"v1/me/top/artists?time_range={time_range}&limit={limit}"

# Define the headers for the requests
def headers(access_token, content_type = "application/json"):
    return {
        "Authorization": f"Bearer {access_token}",
        # "Content-Type": f"{content_type}"
    }

# Get the ID of the currently playing track 
def CurrentTrackID(response):
    return response.json()["item"]["id"]

def likeTrack(track_id, headers, likeurl=apiurl("v1/me/tracks")):
    # Send a PUT request to "like" the currently playing track
    like_payload = json.dumps({"ids": [track_id]})
    like_response = requests.put(likeurl, headers=headers, data=like_payload)
    if like_response.status_code == 200:
            print("Liked the currently playing track!")
    else:
        print("Failed to like the currently playing track.")




def likePlayingTrack(headers, nowplayingurl=apiurl("v1/me/player/currently-playing")):
    # Send a GET request to retrieve the currently playing track
    print(f"nowplayingurl = {nowplayingurl}")
    print(f"headers = {headers}")
    response = requests.get(nowplayingurl, headers=headers)
    print(f"response = {response}")
    
    if response.status_code == 200 and "item" in response.json():
        # Get the ID of the currently playing track
        track_id = CurrentTrackID(response)
        # like the track
        likeTrack(track_id, headers)
    else:
        # No track is currently playing
        print("No track is currently playing.")
        print(response.status_code)
        print(response)





def main():
    # current playing track endpoint
    now_playing_url= apiurl("v1/me/player/currently-playing")
    # like track endpoint
    like_track = apiurl("v1/me/tracks")

    likePlayingTrack(headers(tokenforAna()))


# call the main function
main()


