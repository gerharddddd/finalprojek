import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = os.environ.get('DEBUG', True)
    
    # ====== MYSQL ======
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:romatua2003@localhost/Dewi_LuSi?charset=utf8mb4'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_recycle': 3600,
        'pool_pre_ping': True,
    }
    
    # Upload
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app/static/uploads')
    QR_CODE_FOLDER = os.path.join(BASE_DIR, 'app/static/qr_codes')
    
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB (untuk video)
    
    # ===== FORMAT YANG DIDUKUNG =====
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'jfif', 'bmp', 'svg'}
    ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'webm', 'ogg', 'mov', 'avi', 'mkv', '3gp'}
    ALLOWED_AUDIO_EXTENSIONS = {
        'mp3', 'wav', 'm4a', 'ogg', 'mp4', 'aac', 'flac', 'aiff', 'alac',
        'amr', 'awb', 'opus', 'webm', '3gp', '3g2', 'mpeg', 'mpga', 'jfif',
        'wma', 'ra', 'rm', 'mid', 'midi', 'kar'
    }
    
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300