from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sensor(db.Model):
    __tablename__ = 'sensors'
    
    id = db.Column(db.Integer, primary_key=True)
    kks = db.Column(db.String(50), nullable=False)
    cabinet = db.Column(db.String(100))
    description = db.Column(db.String(200))
    type = db.Column(db.String(10))  # 'AI' или 'BI'
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    min_val = db.Column(db.Float)
    max_val = db.Column(db.Float)
    current_val = db.Column(db.Float)
    unit = db.Column(db.String(20))
    status = db.Column(db.String(20), default='normal')
    
    def to_dict(self):
        """Превращает объект в словарь для JSON"""
        return {
            'id': self.id,
            'kks': self.kks,
            'cabinet': self.cabinet,
            'description': self.description,
            'type': self.type,
            'x': self.x,
            'y': self.y,
            'min_val': self.min_val,
            'max_val': self.max_val,
            'current_val': self.current_val,
            'unit': self.unit,
            'status': self.status
        }