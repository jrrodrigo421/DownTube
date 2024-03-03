# # from flask import Flask, render_template, request, redirect, send_from_directory
# # import pytube
# # import os

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/download', methods=['POST'])
# # def download():
# #     if request.method == 'POST':
# #         video_url = request.form['video_url']
# #         try:
# #             youtube = pytube.YouTube(video_url)
# #             video = youtube.streams.get_highest_resolution()
# #             filename = video.default_filename  # Obtém o nome do arquivo do vídeo
# #             video.download('downloads/')
# #             return redirect('/downloaded/' + filename)  # Redireciona para a página de download com o nome do arquivo
# #         except Exception as e:
# #             return render_template('index.html', error=True)

# # @app.route('/downloaded/<filename>')  # Rota para servir o vídeo baixado
# # def serve_video(filename):
# #     return send_from_directory('downloads/', filename)

# # if __name__ == '__main__':
# #     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, send_from_directory
# import pytube
# import os
# from urllib.parse import unquote

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

# @app.route('/downloaded/<path:filename>')  # Rota para servir o vídeo baixado
# def serve_video(filename):
#     filename = unquote(filename)
#     print('filename >>>',filename)# Decodifica a URL
#     downloads_dir = os.path.abspath('downloads/')  # Obtém o caminho absoluto para a pasta 'downloads/'
#     print('downloads_dir >>> ', downloads_dir)
#     return send_from_directory(downloads_dir, filename, as_attachment=True)  # Serve o arquivo para download

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, send_from_directory
import youtube_dl
import os
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            ydl_opts = {'outtmpl': 'downloads/%(title)s.%(ext)s'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)    
                video_title = info_dict.get('title', None)
                return redirect('/downloaded/' + video_title)
        except Exception as e:
            return render_template('index.html', error=True)

@app.route('/downloaded/<path:filename>')  # Rota para servir o vídeo baixado
def serve_video(filename):
    filename = unquote(filename)
    downloads_dir = os.path.abspath('downloads/')  # Obtém o caminho absoluto para a pasta 'downloads/'
    return send_from_directory(downloads_dir, filename, as_attachment=True)  # Serve o arquivo para download

if __name__ == '__main__':
    app.run(debug=True)
