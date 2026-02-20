# Offline-Privacy-Preserving-Hindi-Voice-Assistant-on-Raspberry-Pi
This project is an offline Hindi voice assistant built using Python, Vosk, and espeak-ng. The system uses a microphone to capture the user's voice input, converts the speech into text using the Vosk speech recognition model, processes the text to understand the user’s intent, and then performs the required action such as telling the time, date, IP address, temperature, playing music, controlling volume, or shutting down the system. The assistant then responds back to the user through speech using espeak-ng. This system works completely offline and is designed to run on a Raspberry Pi using Vosk-supported audio tools and Python libraries.

**Installation**

Clone the repository to your local machine:
       git clone https://github.com/your-username/Offline-Hindi-Voice-Assistant.git
       cd Offline-Hindi-Voice-Assistant

Install the required system dependencies:
       sudo apt update
       sudo apt install -y python3 python3-pip python3-venv \
       portaudio19-dev espeak-ng mpg123 alsa-utils

Create and activate virtual environment (recommended):
       python3 -m venv venv
       source venv/bin/activate

Install the required Python packages:
      pip install -r requirements.txt
      If you don’t have a requirements.txt file, install manually:

pip install vosk pyaudio
      Download the Hindi Vosk model from:
      https://alphacephei.com/vosk/models

Download:
      vosk-model-small-hi-0.22
      Extract the downloaded file and place the model folder inside:

models/
       Final structure should look like:
       Offline-Hindi-Voice-Assistant/
       │
       ├── main.py
       ├── config.py
       ├── core/
       ├── models/
       │   └── vosk-model-small-hi-0.22/
       └── logs/
