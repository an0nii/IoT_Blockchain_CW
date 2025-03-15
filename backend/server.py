from flask import Flask, request, jsonify
from flask_cors import CORS
import pyqrcode
import io
import base64
import zlib

app = Flask(__name__)
CORS(app)

@app.route('/api/generate_qr', methods=['POST'])
def generate_qr():
    try:
        data = request.json.get('data', '')
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        dataCompressZlib = zlib.compress(data.encode('utf-8'))
        QRdata = base64.b64encode(dataCompressZlib)
        
        qr = pyqrcode.create(QRdata)
        buffer = io.BytesIO()
        qr.png(buffer, scale=6)
        buffer.seek(0)
    
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        data_url = f"data:image/png;base64,{img_base64}"
        
        return jsonify({'qrCode': data_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000, debug=True)