from flask import Flask, request, jsonify
import pyclamd

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = f'uploads/{file.filename}'
    file.save(file_path)
    scan_result = scan_file(file_path)
    return jsonify(scan_result)

def scan_file(file_path):
    cd = pyclamd.ClamdAgnostic()
    cd.reload()
    result = cd.scan_file(file_path)
    return result

if __name__ == '__main__':
    app.run(debug=True)
