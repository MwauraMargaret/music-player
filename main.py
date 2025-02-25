import tkinter as tk
import yt_dlp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from pygame import mixer

mixer.init()

canvas = tk.Tk()
canvas.title("Musiki Player")
canvas.geometry("600x800")
canvas.config(bg='black')

def play_youtube():
    url = url_entry.get()
    if url:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
            'outtmpl': 'temp_song.mp3',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        mixer.music.load("temp_song.mp3")
        mixer.music.play()

def play_spotify():
    url = url_entry.get()
    if "spotify" not in url:
        return
    
    CLIENT_ID = ""
    CLIENT_SECRET = ""

    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

    track_id = url.split("/")[-1].split("?")[0]
    track_info = sp.track(track_id)
    preview_url = track_info.get('preview_url')

    if preview_url:
        response = requests.get(preview_url)
        with open("spotify_preview.mp3", "wb") as f:
            f.write(response.content)
        mixer.music.load("spotify_preview.mp3")
        mixer.music.play()

url_entry = tk.Entry(canvas, width=50)
url_entry.pack(pady=5)

yt_button = tk.Button(canvas, text="Play YouTube", command=play_youtube, bg="red", fg="white")
yt_button.pack(pady=5)

spotify_button = tk.Button(canvas, text="Play Spotify", command=play_spotify, bg="green", fg="white")
spotify_button.pack(pady=5)

canvas.mainloop()