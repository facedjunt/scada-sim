from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import random
import time
import threading

app = Flask(__name__)
CORS(app)

#подключение к базе
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kadsu@localhost:5432/scada_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#модель датчика (таблица sensors)
class Sensor(db.Model):
    __tablename__ = 'sensors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    kks = db.Column(db.String(50), nullable=False)
    min_val = db.Column(db.Float, nullable=False)
    max_val = db.Column(db.Float, nullable=False)
    current_val = db.Column(db.Float)
    unit = db.Column(db.String(20))
    type = db.Column(db.String(10))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'kks': self.kks,
            'min_val': self.min_val,
            'max_val': self.max_val,
            'current_val': self.current_val,
            'unit': self.unit,
            'type': self.type
        }

#функция для обновления значений в базе (воркер)
def update_values():
    with app.app_context():
        while True:
            try:
                sensors = Sensor.query.all()
                for sensor in sensors:
                    if sensor.type == 'AI':
                        new_val = round(random.uniform(sensor.min_val, sensor.max_val), 2)
                        sensor.current_val = new_val
                db.session.commit()
                print(f"[{time.strftime('%H:%M:%S')}] Значения обновлены в БД")
            except Exception as e:
                print(f"Ошибка обновления: {e}")
            time.sleep(2)

#запуск воркера в фоне
def start_worker():
    thread = threading.Thread(target=update_values, daemon=True)
    thread.start()

#эндпоинт для получения всех датчиков
@app.route('/api/sensors', methods=['GET'])
def get_sensors():
    sensors = Sensor.query.all()
    return jsonify([s.to_dict() for s in sensors])

#эндпоинт для принудительного обновления
@app.route('/api/update', methods=['POST'])
def force_update():
    sensors = Sensor.query.all()
    for sensor in sensors:
        if sensor.type == 'AI':
            new_val = round(random.uniform(sensor.min_val, sensor.max_val), 2)
            sensor.current_val = new_val
    db.session.commit()
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  #создаст таблицу, если её нет
    start_worker()      #запускаем воркер
    app.run(debug=True, port=5000)