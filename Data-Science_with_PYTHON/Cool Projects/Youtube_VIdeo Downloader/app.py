from flask import Flask, render_template, request, redirect, url_for, flash
from pytubefix import YouTube
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing messages

# Save downloaded videos to a "downloads" folder
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download_video():
    try:
        # Get the URL from the form
        video_url = request.form.get("video_url")
        if not video_url:
            flash("Please provide a YouTube URL!", "error")
            return redirect(url_for("index"))
        
        # Download the video
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(DOWNLOAD_FOLDER)
        
        flash(f"Video downloaded successfully! Check the 'downloads' folder.", "success")
    except Exception as e:
        flash(f"Something went wrong: {str(e)}", "error")
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
