import json
from babel.translation import from_google

def make_marker_dict(text_origin, text_en, code):
    marker = {'Text_origin': text_origin, 'Text_en': text_en, 'Code': code}
    return marker

class TranslationHistory:

    def __init__(self):
        self.history = []

    def add_marker(self, text_origin, code):
        text_en = from_google(text_origin, source=code, target='en')
        marker = make_marker_dict(text_origin, text_en, code)
        self.history.append(marker)

    def to_json(self, filename):
    	json_temp = json.dumps(self.history)
    	file = open(filename, 'w')
    	file.write(json_temp)
    	file.close()