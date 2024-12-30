import threading
import serial
from flask import Flask

# Seri Port Ayarları
SERIAL_PORT = '/dev/ttyUSB0'  # Raspberry Pi'de bağlı cihazın portunu kontrol edin
BAUD_RATE = 9600

def serial_communication():
    """PySerial ile 'Hello World' mesajını gönder."""
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        ser.write(b"Hello World\n")
        print("Serial: Hello World gönderildi.")
        ser.close()
    except Exception as e:
        print(f"Seri port hatası: {e}")

# Flask Web Sunucusu
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Elbaas"

def run_web_server():
    """Flask web sunucusunu başlat."""
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    # Seri iletişim için bir thread oluştur
    serial_thread = threading.Thread(target=serial_communication)
    serial_thread.start()

    # Web sunucusunu çalıştır
    run_web_server()
