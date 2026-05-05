import random
import time
from app import app  # импортируем настройки из app.py
from models import db, Sensor

def update_sensor_values():
    """Функция, которая обновляет значения датчиков"""
    with app.app_context():  # нужно, чтоб работать с БД внутри Flask
        sensors = Sensor.query.all()
        for sensor in sensors:
            if sensor.type == 'AI':  # аналоговый сигнал
                # Генерим случайное значение в пределах min-max
                new_val = round(random.uniform(sensor.min_val, sensor.max_val), 2)
                sensor.current_val = new_val
                
                # Определяем статус
                range_size = sensor.max_val - sensor.min_val
                if sensor.current_val < sensor.min_val + range_size * 0.3:
                    sensor.status = 'low'
                elif sensor.current_val > sensor.max_val - range_size * 0.3:
                    sensor.status = 'high'
                else:
                    sensor.status = 'normal'
            
            # Для дискретных сигналов (BI) - просто 0 или 1
            else:
                sensor.current_val = random.randint(0, 1)
                sensor.status = 'normal' if sensor.current_val == 1 else 'alarm'
        
        db.session.commit()
        print(f"[{time.strftime('%H:%M:%S')}] Значения обновлены")

if __name__ == '__main__':
    print("Воркер запущен, обновляем каждые 2 секунды...")
    while True:
        update_sensor_values()
        time.sleep(2)  # ждём 2 секунды [citation:5]