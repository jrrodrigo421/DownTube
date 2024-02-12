from flask import Flask, render_template, request, redirect
import pytube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            youtube = pytube.YouTube(video_url)
            video = youtube.streams.get_highest_resolution()
            video.download('downloads/')
            return redirect('/')
        except Exception as e:
            return render_template('index.html', error=True)

if __name__ == '__main__':
    app.run(debug=True)
