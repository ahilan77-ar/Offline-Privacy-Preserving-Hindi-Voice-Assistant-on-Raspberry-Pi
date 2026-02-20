import os

class TTS:
    def speak(self, text):
        print("Assistant:", text)
        os.system(f'espeak-ng -v hi "{text}"')
