from flask import Flask, render_template, request, send_file
import boto3
from io import BytesIO

app = Flask(__name__)

# Initialize Polly client
polly = boto3.client('polly')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']
    response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')
    
    audio_stream = response.get("AudioStream")
    return send_file(BytesIO(audio_stream.read()), mimetype='audio/mpeg', as_attachment=True, attachment_filename='output.mp3')

if __name__ == '__main__':
    app.run(debug=True)
