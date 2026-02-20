import json
import pyaudio
from vosk import Model, KaldiRecognizer
from config import MODEL_PATH, SAMPLE_RATE

class ASR:
    def __init__(self):
        self.model = Model(MODEL_PATH)
        self.recognizer = KaldiRecognizer(self.model, SAMPLE_RATE)

        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=SAMPLE_RATE,
                                    input=True,
                                    frames_per_buffer=8192)
        self.stream.start_stream()

    def listen(self):
        while True:
            data = self.stream.read(4096, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                return result.get("text", "")
