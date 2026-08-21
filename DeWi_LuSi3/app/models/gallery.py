from app import db
from datetime import datetime

class Gallery(db.Model):
    __tablename__ = 'gallery'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    photo_path = db.Column(db.String(500), nullable=False)
    caption = db.Column(db.String(200))
    category = db.Column(db.String(50), default='desa')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Gallery {self.title}>'