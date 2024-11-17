import socket
import serial
import requests

# ===============================
# COMMON PROTOCOL TEMPLATES
# ===============================

# 1. HTTP
def connect_http(url, params=None):
    """
    Template for HTTP communication.
    """
    try:
        response = requests.get(url, params=params)
        return response.text
    except Exception as e:
        print(f"HTTP Connection Error: {e}")
        return None

# 2. WebSocket
import websocket

def connect_websocket(url):
    """
    Template for WebSocket communication.
    """
    try:
        ws = websocket.WebSocket()
        ws.connect(url)
        return ws
    except Exception as e:
        print(f"WebSocket Connection Error: {e}")
        return None

# 3. TCP
def connect_tcp(host, port):
    """
    Template for TCP socket connection.
    """
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        return client_socket
    except Exception as e:
        print(f"TCP Connection Error: {e}")
        return None

# 4. UDP
def connect_udp(host, port):
    """
    Template for UDP socket connection.
    """
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return udp_socket, (host, port)
    except Exception as e:
        print(f"UDP Connection Error: {e}")
        return None

# 5. Serial (UART)
def connect_serial(port, baudrate):
    """
    Template for serial communication (UART).
    """
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        return ser
    except Exception as e:
        print(f"Serial Connection Error: {e}")
        return None

# ===============================
# PROTOCOLS FOR ROBOTICS
# ===============================

# 6. I2C (Inter-Integrated Circuit)
def connect_i2c(bus_id):
    """
    Template for I2C communication.
    """
    try:
        import smbus
        bus = smbus.SMBus(bus_id)
        return bus
    except Exception as e:
        print(f"I2C Connection Error: {e}")
        return None

# 7. SPI (Serial Peripheral Interface)
def connect_spi():
    """
    Template for SPI communication.
    """
    try:
        import spidev
        spi = spidev.SpiDev()
        spi.open(0, 0)  # Bus 0, Device 0 (modify as needed)
        spi.max_speed_hz = 500000
        return spi
    except Exception as e:
        print(f"SPI Connection Error: {e}")
        return None

# 8. CAN (Controller Area Network)
def connect_can(interface):
    """
    Template for CAN communication.
    """
    try:
        import can
        bus = can.interface.Bus(interface, bustype='socketcan')
        return bus
    except Exception as e:
        print(f"CAN Connection Error: {e}")
        return None

# ===============================
# OTHER PROTOCOLS
# ===============================

# 9. MQTT
import paho.mqtt.client as mqtt

def connect_mqtt(broker, port=1883):
    """
    Template for MQTT communication.
    """
    try:
        client = mqtt.Client()
        client.connect(broker, port, 60)
        return client
    except Exception as e:
        print(f"MQTT Connection Error: {e}")
        return None

# 10. FTP
from ftplib import FTP

def connect_ftp(host, username, password):
    """
    Template for FTP connection.
    """
    try:
        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        return ftp
    except Exception as e:
        print(f"FTP Connection Error: {e}")
        return None

# ===============================
# EXAMPLE USAGE
# ===============================

if __name__ == "__main__":
    # Example: Connect to an HTTP server
    print(connect_http("https://api.example.com/data"))

    # Example: Connect to a WebSocket server
    ws = connect_websocket("ws://example.com/socket")
    if ws:
        ws.send("Hello, WebSocket!")
        print(ws.recv())
        ws.close()

    # Example: Open a serial connection
    serial_conn = connect_serial("COM3", 9600)
    if serial_conn:
        serial_conn.write(b'Hello, UART!')
        print(serial_conn.readline())
