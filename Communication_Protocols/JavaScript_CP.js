const net = require("net");
const dgram = require("dgram");
const http = require("http");
const WebSocket = require("ws");
const SerialPort = require("serialport");

// ===============================
// COMMON PROTOCOL TEMPLATES
// ===============================

// 1. HTTP
function connectHTTP(host, path = "/") {
  const options = {
    hostname: host,
    port: 80,
    path: path,
    method: "GET",
  };

  const req = http.request(options, (res) => {
    let data = "";
    res.on("data", (chunk) => {
      data += chunk;
    });

    res.on("end", () => {
      console.log("HTTP Response:", data);
    });
  });

  req.on("error", (err) => {
    console.error("HTTP Error:", err.message);
  });

  req.end();
}

// 2. WebSocket
function connectWebSocket(url) {
  const ws = new WebSocket(url);

  ws.on("open", () => {
    console.log("WebSocket connection established.");
    ws.send("Hello, WebSocket!");
  });

  ws.on("message", (data) => {
    console.log("WebSocket Message:", data);
  });

  ws.on("error", (err) => {
    console.error("WebSocket Error:", err.message);
  });
}

// 3. TCP
function connectTCP(host, port) {
  const client = new net.Socket();

  client.connect(port, host, () => {
    console.log("TCP Connection established.");
    client.write("Hello, TCP!");
  });

  client.on("data", (data) => {
    console.log("TCP Data:", data.toString());
  });

  client.on("error", (err) => {
    console.error("TCP Error:", err.message);
  });

  client.on("close", () => {
    console.log("TCP Connection closed.");
  });
}

// 4. UDP
function connectUDP(host, port) {
  const client = dgram.createSocket("udp4");
  const message = Buffer.from("Hello, UDP!");

  client.send(message, port, host, (err) => {
    if (err) {
      console.error("UDP Error:", err.message);
    } else {
      console.log("UDP Message sent.");
    }
    client.close();
  });
}

// ===============================
// PROTOCOLS FOR ROBOTICS
// ===============================

// 5. Serial (UART)
function connectSerial(port, baudRate) {
  const serial = new SerialPort(port, { baudRate: baudRate });

  serial.on("open", () => {
    console.log("Serial port opened.");
    serial.write("Hello, UART!");
  });

  serial.on("data", (data) => {
    console.log("Serial Data:", data.toString());
  });

  serial.on("error", (err) => {
    console.error("Serial Error:", err.message);
  });
}

// 6. I2C
function connectI2C() {
  console.error("I2C requires a library like i2c-bus or Johnny-Five.");
}

// 7. SPI
function connectSPI() {
  console.error("SPI requires a library like spi-device.");
}

// 8. CAN
function connectCAN() {
  console.error("CAN requires a library like socketcan.");
}

// ===============================
// OTHER PROTOCOLS
// ===============================

// 9. MQTT
function connectMQTT(broker, port) {
  console.error("MQTT requires a library like mqtt.js.");
}

// 10. FTP
function connectFTP(host, username, password) {
  console.error("FTP requires a library like basic-ftp or node-ftp.");
}

// ===============================
// EXAMPLE USAGE
// ===============================

async function exampleUsage() {
  // Example: Connect to an HTTP server
  console.log("Connecting to HTTP server...");
  connectHTTP("example.com");

  // Example: Connect to a WebSocket server
  console.log("Connecting to WebSocket server...");
  connectWebSocket("ws://echo.websocket.org");

  // Example: Connect to a TCP server
  console.log("Connecting to TCP server...");
  connectTCP("127.0.0.1", 3000);

  // Example: Connect to a UDP server
  console.log("Connecting to UDP server...");
  connectUDP("127.0.0.1", 12345);

  // Example: Connect to a Serial port
  console.log("Connecting to Serial port...");
  connectSerial("/dev/ttyUSB0", 9600);
}

exampleUsage();
