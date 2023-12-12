# Imports necesarios
import network
from time import sleep
from umqtt.simple import MQTTClient  # Importa solo lo necesario de umqtt.simple
from machine import Pin, PWM

# Definición de pines para el motor
IN1 = Pin(26, Pin.OUT)
IN2 = Pin(25, Pin.OUT)
IN3 = Pin(33, Pin.OUT)
IN4 = Pin(32, Pin.OUT)

from machine import Pin, PWM
import time

sg90 = PWM(Pin(13, mode=Pin.OUT))
sg90.freq(50)


pins = [IN1, IN2, IN3, IN4]

# Secuencias de pasos para el motor
secuencia1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
secuencia2 = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]

# Configuración de MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/elefante/proy"
MQTT_PORT = 1883  # Cambiado a tipo de dato int

def wifi_connect():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("UTNG_Alumnos", "")
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi conectada")

def llegada_mensaje(topic, msg):
    print(msg)
    if msg == b'encender':
        led.value(0)
        print(msg)
    elif msg == b'apagar':
        led.value(1)
        print(msg)
    elif msg == b'mover':
        try:
            for _ in range(512):
                for step in secuencia2:
                    for i in range(len(pins)):
                        pins[i].value(step[i])
                        sleep(0.001)
            sleep(1)
            for _ in range(512):
                for step in secuencia1:
                    for i in range(len(pins)):
                        pins[i].value(step[i])
                        sleep(0.001)
        except Exception as e:
            print("Error en la secuencia del motor:", e)
            
    elif msg== b'servo':
        sg90.duty(40)    # Establecer el ciclo de trabajo para mover el servo a 0 grados
        time.sleep(2)    # Esperar 2 segundos (aumentado para un movimiento más lento)
        sg90.duty(115)    # Establecer el ciclo de trabajo para mover el servo a 45 grados
        time.sleep(2)    # Esperar 2 segundos (aumentado para un movimiento más lento)
        sg90.duty(30)    # Volver el servo a 0 grados
        time.sleep(2)    # Esperar 2 segundos (aumentado para un movimiento más lento)

def suscribir():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT,
                        user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado en %s, al topico %s" % (MQTT_BROKER, MQTT_TOPIC))
    return client

# Configuración del LED Amarillo
led = Pin(2, Pin.OUT)
led.value(1)

# Conexión WiFi y suscripción MQTT
wifi_connect()
client = suscribir()

# Bucle principal
while True:
    client.check_msg()
    sleep(2)
