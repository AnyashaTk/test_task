import json
import re

from vosk import Model, KaldiRecognizer


class SpeechRecognizeWorker:
    def __init__(self):
        self.sd = None
        self.rec = None
        super(SpeechRecognizeWorker, self).__init__()

    def run(self, audio, model):
        full_text = ''

        self.rec = KaldiRecognizer(model, 16000)
        self.rec.SetWords(True)
        while True:
            # не трогаем метадату
            data = audio.read(4000)
            if len(data) == 0:
                break
            else:
                if self.rec.AcceptWaveform(data):
                    recognized_data = self.rec.Result()
                    recognized_data = json.loads(recognized_data)
                    voice_input_str = recognized_data["text"]
                    if voice_input_str != "":
                        print(recognized_data['result'])
                        words = ''
                        for dict_i in recognized_data['result']:
                            words += dict_i['word'] + ' '
                        full_text += words + '\n'

        final_list = full_text
        print('result: ', final_list)
        return final_list
