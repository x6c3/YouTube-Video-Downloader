from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)
@app.route("/")
def thing():
    return '<a href="/home">Click here lmao</a>'

@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])

def download():
    if request.method == 'POST':
        link = request.form['link-name']
        try:
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path='downloads')
            return '<script>alert("successfully downlaoded the video");</script>' + render_template('index.html')
        except Exception as e:
            print(f'something occurred {e}')



if __name__ == '__main__':
    app.run(debug=True)
