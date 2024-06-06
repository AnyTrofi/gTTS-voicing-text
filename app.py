from flask import Flask, request, send_file
from gtts import gTTS
import tempfile
import io
import config

app = Flask(__name__)

@app.route('/say', methods=['POST'])
def text_to_speech():
    data = request.json
    text = str(data.get('text'))
    language = str(data.get('language'))
    speed = data.get('speed', False)

    if not text:
        return {'error': 'Text are required.'}, 400

    if not language:
        language = 'en'

    speech = gTTS(text=text, lang=language, slow=speed)

    audio_file = tempfile.NamedTemporaryFile(delete=True, suffix='.wav')
    speech.save(audio_file.name)

    audio_file.seek(0)
    return send_file(audio_file, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(host=config.IP, port=config.PORT)
else:
    application = app