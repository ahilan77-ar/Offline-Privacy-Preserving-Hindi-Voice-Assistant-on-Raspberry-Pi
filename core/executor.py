import os
import socket
import subprocess
import datetime

class Executor:

    def execute(self, intent):

        if intent == "time":
            return f"अभी समय है {datetime.datetime.now().strftime('%H:%M')}"

        elif intent == "date":
            return f"आज की तारीख है {datetime.datetime.now().strftime('%d %B %Y')}"

        elif intent == "greet":
            return "नमस्ते, मैं आपकी सहायता के लिए तैयार हूँ"

        elif intent == "status":
            return "मैं ठीक हूँ, धन्यवाद"

        elif intent == "ip":
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return f"आपका आईपी एड्रेस है {ip}"

        elif intent == "temperature":
            temp = subprocess.check_output(
                ["vcgencmd", "measure_temp"]
            ).decode()
            temp = temp.replace("temp=", "").replace("'C\n", "")
            return f"सीपीयू तापमान {temp} डिग्री है"

        elif intent == "music":
            os.system("mpg123 song.mp3 &")
            return "गाना चला रहा हूँ"

        elif intent == "vol_up":
            os.system("amixer set Master 10%+")
            return "वॉल्यूम बढ़ा दिया"

        elif intent == "vol_down":
            os.system("amixer set Master 10%-")
            return "वॉल्यूम कम किया"

        elif intent == "restart":
            os.system("sudo reboot")
            return "सिस्टम रीस्टार्ट हो रहा है"

        elif intent == "shutdown":
            os.system("sudo shutdown now")
            return "सिस्टम बंद हो रहा है"

        elif intent == "exit":
            return "assistant_exit"

        else:
            return "मुझे समझ में नहीं आया"
