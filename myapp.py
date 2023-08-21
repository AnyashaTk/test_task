from flask import Flask, request, jsonify, render_template, send_file
from pydub import AudioSegment
# import speech_recognition as sr
from recognizer import SpeechRecognizeWorker
from vosk import Model

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/modify-audio', methods=['POST'])
def modify_audio():
    print('modifying..')
    audio_file = request.files['audio']
    speed = float(request.form['speed'])
    volume = float(request.form['volume'])

    audio = AudioSegment.from_wav(audio_file)
    modified_audio = audio.speedup(playback_speed=speed).apply_gain(volume)

    modified_audio.export('modified_audio.wav', format='wav')

    print('modifying process has ended')
    modified_audio.export('modified_audio.wav', format='wav')

    return send_file('modified_audio.wav', as_attachment=True)


@app.route('/transcribe-audio', methods=['POST'])
def transcribe_audio():
    print('recognizing..')
    audio_file = request.files['audio']
    language = request.form['language']

    recognizer = SpeechRecognizeWorker()
    if language == 'english':
        model = Model("./vosk_en-us_little")
        transcript = recognizer.run(audio_file, model=model)
    elif language == 'russian':
        model = Model("./vosk_rus_little")
        transcript = recognizer.run(audio_file, model=model)
    else:
        return jsonify({'error': 'Invalid language'})

    print('recognizing process has ended')
    return jsonify({'transcript': transcript})


if __name__ == '__main__':
    app.run()
