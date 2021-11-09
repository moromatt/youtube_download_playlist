import os
import subprocess

from pytube import Playlist, YouTube

def run(pl):
    filepath = os.path.dirname(os.path.realpath(__file__)) + "/output/"
    os.makedirs(filepath, exist_ok=True)
    # get linked list of links in the playlist
    links = pl.video_urls
    # download each item in the list
    for l in links:
        # converts the link to a YouTube object
        yt = YouTube(l)
        # takes audio stream
        music = yt.streams.get_audio_only()
        print("Downloading " + music.default_filename + "...")
        music.download(filepath)
    
    print("Download finished.")

if __name__ == "__main__":
    url = input("Please enter the url of the playlist you wish to download: ")
    pl = Playlist(url)
    run(pl)