from flask import Flask,request

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f'upload/{file.filename}')
    return 'File Uploaded', 200

if __name__ == '__main__':
    app.run(debug=True)


