from flask import Flask, render_template, request, redirect, url_for, flash
from pytubefix import YouTube
from pydub import AudioSegment
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing messages

# Save downloaded content to a "downloads" folder
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download_video():
    try:
        # Get the URL and download option (video or audio) from the form
        video_url = request.form.get("video_url")
        download_audio = request.form.get("download_audio")  # If 'download_audio' is checked
        
        if not video_url:
            flash("Please provide a YouTube URL!", "error")
            return redirect(url_for("index"))

        yt = YouTube(video_url)
        
        if download_audio:
            # Download the audio stream (audio only)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_file_path = os.path.join(DOWNLOAD_FOLDER, yt.title + '.webm')  # Download as .webm (audio format)
            audio_stream.download(output_path=DOWNLOAD_FOLDER, filename=yt.title + '.webm')

            # Convert the downloaded .webm audio file to MP3 using pydub
            audio = AudioSegment.from_file(audio_file_path)
            mp3_file_path = os.path.join(DOWNLOAD_FOLDER, yt.title + '.mp3')
            audio.export(mp3_file_path, format="mp3")

            # Optional: Remove the original .webm file after conversion
            os.remove(audio_file_path)

            flash(f"Audio downloaded and converted to MP3 successfully! Check the 'downloads' folder.", "success")
        
        else:
            # Download the video (highest resolution)
            stream = yt.streams.get_highest_resolution()
            stream.download(DOWNLOAD_FOLDER)
            flash(f"Video downloaded successfully! Check the 'downloads' folder.", "success")

    except Exception as e:
        flash(f"Something went wrong: {str(e)}", "error")
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
