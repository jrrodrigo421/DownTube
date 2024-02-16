# from flask import Flask, render_template, request, redirect, send_from_directory
# import pytube

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/download', methods=['POST'])
# def download():
#     if request.method == 'POST':
#         video_url = request.form['video_url']
#         try:
#             youtube = pytube.YouTube(video_url)
#             video = youtube.streams.get_highest_resolution()
#             video.download('downloads/')
#             return redirect('/')
#         except Exception as e:
#             return render_template('index.html', error=True)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, send_from_directory
import pytube
import os

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
            filename = video.default_filename  # Obtém o nome do arquivo do vídeo
            video.download('downloads/')
            return redirect('/downloaded/' + filename)  # Redireciona para a página de download com o nome do arquivo
        except Exception as e:
            return render_template('index.html', error=True)

@app.route('/downloaded/<filename>')  # Rota para servir o vídeo baixado
def serve_video(filename):
    return send_from_directory('downloads/', filename)

if __name__ == '__main__':
    app.run(debug=True)