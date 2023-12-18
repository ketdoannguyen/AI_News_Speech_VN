from io import BytesIO

import pandas as pd
import pygame
import requests
import re


class AudioPlayerSpeech():
    def __init__(self):
        self.list_url = pd.read_csv("./dataset/URL_audio_from_api.csv")

        # Initialize pygame
        pygame.init()
        # Initialize the audio module
        pygame.mixer.init()

    def init(self,index, person, path_save):
        self.is_paused = False
        self.response = requests.get(self.list_url[person][index])
        self.path_save = path_save + " " + person

        audio_file = BytesIO(self.response.content)
        # response.close()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()
        self.is_paused = True

    def unpause(self):
        pygame.mixer.music.unpause()
        self.is_paused = False

    def download(self):
        vietnam_char = "ABCDEFGHIJKLMNOPQRSTUVXYZÀÁẢÃĂẠẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ"

        try:
            pattern = re.compile(r"[^"+vietnam_char+vietnam_char.lower()+"0-9]")
            self.path_save = "./audio_download/" + re.sub(pattern, '_', self.path_save) + ".mp3"
            with open(self.path_save, 'wb') as audio_file:
                audio_file.write(self.response.content)
            print(f"Audio downloaded and saved to {self.path_save}")
        except:
            print(f"Failed to download audio. Status code: {self.response.status_code}")


