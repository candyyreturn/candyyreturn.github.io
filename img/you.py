from pytube import YouTube
import subprocess, os, sys

import random
import string

def generate_random_text(length):
    characters = string.ascii_lowercase
    text = ''.join(random.choice(characters) for _ in range(length))
    return text

random_text = generate_random_text(8)+".mp3"

print("Filename: ",random_text)

def Download(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()

        # Obtener el nombre del archivo descargado
        video_filename = youtubeObject.default_filename

        # Convertir el archivo descargado de MP4 a MP3
        audio_filename = os.path.splitext(video_filename)[0] + ".mp3"
        subprocess.run(['ffmpeg', '-i', video_filename, audio_filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Eliminar el archivo MP4
        os.remove(video_filename)
        os.rename(audio_filename, random_text)

        print("Download and conversion completed successfully.")
    except Exception as e:
        print("An error has occurred:", str(e))

link = sys.argv[1]
Download(link)
