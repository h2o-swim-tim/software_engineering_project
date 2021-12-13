from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.
def index(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='7ab9923626ae4b8c88822e69eea08dc1',
        client_secret='87e6195e67a54bfa845089e09e3626ed',))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks'][:10]
        return render(request,'base.html',{"results":final_result})
    else:
      return render(request,'base.html',)

def cal_index(request):
    page_token = None
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
    for event in events['items']:
        print event['summary']
    page_token = events.get('nextPageToken')
    if not page_token:
        break