from flask import Flask, request, render_template, send_file
import boto3
from io import BytesIO

app = Flask(__name__)

# Initialize Amazon Polly client
polly = boto3.client('polly')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )
    audio_stream = response['AudioStream']
    
    # Create a BytesIO object to hold the audio stream
    audio_bytes = BytesIO(audio_stream.read())

    # Return the audio file as an attachment
    return send_file(audio_bytes, mimetype='audio/mpeg', as_attachment=True, download_name='output.mp3')

if __name__ == '__main__':
    app.run(debug=True)
