from core.asr import ASR
from core.tts import TTS
from core.nlp import IntentParser
from core.executor import Executor
from config import LOG_FILE
import time

def log_interaction(user, response):
    with open(LOG_FILE, "a") as f:
        f.write(f"User: {user}\nAssistant: {response}\n\n")

def main():

    asr = ASR()
    tts = TTS()
    parser = IntentParser()
    executor = Executor()

    tts.speak("ऑफलाइन हिंदी वॉयस असिस्टेंट शुरू हो गया है")

    while True:
        text = asr.listen()

        if not text:
            continue

        print("You:", text)

        intent = parser.parse(text)
        response = executor.execute(intent)

        if response == "assistant_exit":
            tts.speak("अलविदा")
            break

        tts.speak(response)
        log_interaction(text, response)

if __name__ == "__main__":
    main()