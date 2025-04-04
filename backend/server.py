from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pyqrcode
import io
import base64
import zlib

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iotadmin:password@localhost:5432/iotdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(42), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "address": self.address,
            "description": self.description
        }

with app.app_context():
    db.create_all()

@app.route('/api/devices', methods=['GET'])
def get_devices():
    try:
        devices = Device.query.all()
        return jsonify({"devices": [d.as_dict() for d in devices]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/devices', methods=['POST'])
def create_device():
    try:
        data = request.json
        existing = Device.query.filter_by(address=data.get('address')).first()
        if existing:
            return jsonify({"device": existing.as_dict(), "message": "Device already exists."}), 200
        new_device = Device(
            name=data.get('name'),
            type=data.get('type'),
            address=data.get('address'),
            description=data.get('description')
        )
        db.session.add(new_device)
        db.session.commit()
        return jsonify({"device": new_device.as_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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