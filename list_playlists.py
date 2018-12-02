
# shows a user's playlists (need to be authenticated via oauth)

import sys
import os
import spotipy
import spotipy.util as util

def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    scope='playlist-read-private'
    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            print playlist['name'], playlist['owner']['id'], playlist['tracks']['total']
            # owner = playlist['owner']['id']
            # results = sp.user_playlist(owner, playlist['id'], fields="tracks,next")
            # tracks = results['tracks']
            # show_tracks(tracks)
            # while tracks['next']:
            #     tracks = sp.next(tracks)
            #     show_tracks(tracks)
    else:
        print("Can't get token for", username)

