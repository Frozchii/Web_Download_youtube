from flask import Flask , render_template , request , jsonify, send_file , after_this_request
from downloader import download_video
import os 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/download" , methods = ["POST"])
def download():
    url = request.form.get("url")
    pilih = request.form.get("pilih")

    result = download_video(url , pilih)

    print("ini file pathnya " ,result["file_Path"])
    @after_this_request
    def cleanup(response) :
        print(type(response))
        print(response)
        print("ini response headernya" , response.headers)
        os.remove(result["file_Path"])
        return response


    return send_file(result["file_Path"] , as_attachment=True , download_name=result["title"]+ result["typeFile"] )



if __name__ == "__main__":
    app.run(debug=True)