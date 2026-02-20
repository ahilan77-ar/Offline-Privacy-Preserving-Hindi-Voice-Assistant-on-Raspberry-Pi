import datetime

class IntentParser:

    def parse(self, text):

        if "समय" in text:
            return "time"

        elif "तारीख" in text:
            return "date"

        elif "नमस्ते" in text:
            return "greet"

        elif "कैसे हो" in text:
            return "status"

        elif "आईपी" in text:
            return "ip"

        elif "तापमान" in text:
            return "temperature"

        elif "गाना" in text:
            return "music"

        elif "वॉल्यूम बढ़ाओ" in text:
            return "vol_up"

        elif "वॉल्यूम कम" in text:
            return "vol_down"

        elif "रीस्टार्ट" in text:
            return "restart"

        elif "सिस्टम बंद" in text:
            return "shutdown"

        elif "बंद करो" in text:
            return "exit"

        else:
            return "unknown"
