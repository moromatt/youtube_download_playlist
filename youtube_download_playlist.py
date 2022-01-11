import os
import subprocess
from pytube import Playlist, YouTube

def get_video(url):
    # converts the link to a YouTube object
    yt = YouTube(url)
    # takes audio stream
    music = yt.streams.get_audio_only()
    print("Downloading " + music.default_filename + "...")
    music.download(filepath)
        # Converting
    file_mp4 = filepath + music.default_filename[:-4] + ".mp4"
    file_mp3 = filepath + music.default_filename[:-4] + ".mp3"
    ffmpeg = ("ffmpeg -i \"" + file_mp4 + "\" \"" + file_mp3 + "\"")
    subprocess.call(ffmpeg, shell=True)
    os.remove(file_mp4)

def run(pl):
    # get linked list of links in the playlist
    links = pl.video_urls
    # download each item in the list
    for link in links:
        get_video(link)
    print("Download finished.")

if __name__ == "__main__":
    url = input("Please enter the url of the playlist you wish to download: ")
    pl = Playlist(url)
    
    filepath = os.path.dirname(os.path.realpath(__file__)) + "/output/"
    os.makedirs(filepath, exist_ok=True)

    if len(pl) == 0: 
        print("The pasted url is for a single YouTube video, converting..")
        get_video(url)
    else:
        print("The pasted url is for a YouTube video playlist, converting..")
        run(pl)
