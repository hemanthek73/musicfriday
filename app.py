from flask import Flask, request, jsonify
from music import play_song, pause_song, stop_song, next_song, prev_song, load_songs, get_current_song
import os

app = Flask(__name__)

# Endpoint to load songs into the playlist
@app.route('/load_songs', methods=['POST'])
def load_music():
    files = request.json.get('files', [])
    # Assuming the files are provided as paths
    load_songs(files)
    return jsonify({"message": "Songs loaded successfully", "files": files})

# Endpoint to play a song
@app.route('/play', methods=['POST'])
def play():
    play_song()
    return jsonify({"message": "Song playing", "current_song": get_current_song()})

# Endpoint to pause/resume a song
@app.route('/pause', methods=['POST'])
def pause():
    pause_song()
    return jsonify({"message": "Song paused/resumed", "current_song": get_current_song()})

# Endpoint to stop a song
@app.route('/stop', methods=['POST'])
def stop():
    stop_song()
    return jsonify({"message": "Song stopped"})

# Endpoint to go to the next song
@app.route('/next', methods=['POST'])
def next():
    next_song()
    return jsonify({"message": "Next song playing", "current_song": get_current_song()})

# Endpoint to go to the previous song
@app.route('/prev', methods=['POST'])
def prev():
    prev_song()
    return jsonify({"message": "Previous song playing", "current_song": get_current_song()})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
