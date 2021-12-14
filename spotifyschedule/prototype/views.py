from __future__ import print_function
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken

import datetime
import os.path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Create your views here.
def index(request):
    if request.method=='POST':
        number = request.POST.get('num')
        num = float(number) * 60 #switching hours to minutes
        num = int (num/4) #get the number of songs 
        #artist_uri = '0YC192cP3KPCRWx8zr8MfZ' #picked artist
        playlist_uri = '37i9dQZF1DWZeKCadgRdKQ'
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='7ab9923626ae4b8c88822e69eea08dc1',
        client_secret='87e6195e67a54bfa845089e09e3626ed'))
        results = spotify.playlist_items(playlist_uri,
                                 additional_types=['track'])
        #results = spotify.artist_top_tracks(artist_uri)
        final_result=results['items'][:num]
        #[:num]
        return render(request,'base.html',{"results":final_result})
    else:
      return render(request,'base.html')

def cal_index(request):
    social_token = SocialToken.objects.get(account__user=request.user)
    creds = Credentials(token=social_token.token,
                    refresh_token= social_token.token_secret,
                    token_uri = 'https://oauth2.googleapis.com/token',
                    client_id=social_token.app.client_id,
                    client_secret=social_token.app.secret)
    """ creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'prototype/credentials.json',  ['https://www.googleapis.com/auth/calendar'])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json()) """
    service = build('calendar', 'v3', credentials= creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    event_count = len(events)

    return render(request, 'base2.html', {"events":event_count})