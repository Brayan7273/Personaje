from hcsr04 import HCSR04
from machine import Pin, PWM
from time import sleep_ms
import time

# Configuración del buzzer
buzzer = PWM(Pin(12), freq=1, duty=0)  # Inicializa el buzzer con frecuencia 0

# Configuración del sensor de ultrasonido
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=24000)

# Configuración del LED Amarillo
led = Pin(26, Pin.OUT)

def reproducir_nota(frecuencia, duracion):
    if frecuencia > 0:
        buzzer.freq(frecuencia)
        buzzer.duty(512)
        sleep_ms(duracion)
    buzzer.duty(0)

def reproducir_melodia(melodia):
    for nota in melodia:
        frecuencia, duracion = nota
        reproducir_nota(frecuencia, duracion)
        sleep_ms(50)  # Pausa breve entre notas

# Melodía de ejemplo 1
melodia_navidad_1 = [
    (523, 400), (523, 400), (523, 800),  # Do
    (523, 400), (523, 400), (523, 800),  # Do
    (523, 400), (587, 400), (523, 400),  # Re
    (523, 400), (523, 400), (523, 800),  # Do
    (587, 400), (659, 400), (659, 800),  # Mi
]

# Melodía de ejemplo 2
melodia_navidad_2 = [
    (659, 400), (659, 400), (659, 800),  # Mi
    (659, 400), (587, 400), (523, 800),  # Re
    (587, 400), (587, 400), (587, 800),  # Re
    (587, 400), (523, 400), (523, 800),  # Do
    (523, 400), (523, 400), (523, 800),  # Do
]

# Melodía de ejemplo 3
melodia_navidad_3 = [
    (523, 400), (587, 400), (523, 400),  # Do, Re, Do
    (659, 400), (587, 400), (523, 800),  # Mi, Re, Do
    (523, 400), (587, 400), (523, 400),  # Do, Re, Do
    (659, 400), (587, 400), (523, 800),  # Mi, Re, Do
    (523, 400), (587, 400), (523, 400),  # Do, Re, Do
]

# Melodía de ejemplo 4
melodia_navidad_4 = [
    (587, 400), (659, 400), (523, 400),  # Re, Mi, Do
    (523, 400), (659, 400), (587, 800),  # Do, Mi, Re
    (587, 400), (659, 400), (523, 400),  # Re, Mi, Do
    (523, 400), (659, 400), (587, 800),  # Do, Mi, Re
    (523, 400), (659, 400), (523, 400),  # Do, Mi, Do
]

# Frecuencias de las notas adicionales
NOTE_B0 = 31
NOTE_C1 = 33
NOTE_CS1 = 35
NOTE_D1 = 37
NOTE_DS1 = 39
NOTE_E1 = 41
NOTE_F1 = 44
NOTE_FS1 = 46
NOTE_G1 = 49
NOTE_GS1 = 52
NOTE_A1 = 55
NOTE_AS1 = 58
NOTE_B1 = 62
NOTE_C2 = 65
NOTE_CS2 = 69
NOTE_D2 = 73
NOTE_DS2 = 78
NOTE_E2 = 82
NOTE_F2 = 87
NOTE_FS2 = 93
NOTE_G2 = 98
NOTE_GS2 = 104
NOTE_A2 = 110
NOTE_AS2 = 117
NOTE_B2 = 123
NOTE_C3 = 131
NOTE_CS3 = 139
NOTE_D3 = 147
NOTE_DS3 = 156
NOTE_E3 = 165
NOTE_F3 = 175
NOTE_FS3 = 185
NOTE_G3 = 196
NOTE_GS3 = 208
NOTE_A3 = 220
NOTE_AS3 = 233
NOTE_B3 = 247
NOTE_C4 = 262
NOTE_CS4 = 277
NOTE_D4 = 294
NOTE_DS4 = 311
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_FS4 = 370
NOTE_G4 = 392
NOTE_GS4 = 415
NOTE_A4 = 440
NOTE_AS4 = 466
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_CS5 = 554
NOTE_D5 = 587
NOTE_DS5 = 622
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_FS5 = 740
NOTE_G5 = 784
NOTE_GS5 = 831
NOTE_A5 = 880
NOTE_AS5 = 932
NOTE_B5 = 988
NOTE_C6 = 1047
NOTE_CS6 = 1109
NOTE_D6 = 1175
NOTE_DS6 = 1245
NOTE_E6 = 1319
NOTE_F6 = 1397
NOTE_FS6 = 1480
NOTE_G6 = 1568
NOTE_GS6 = 1661
NOTE_A6 = 1760
NOTE_AS6 = 1865
NOTE_B6 = 1976
NOTE_C7 = 2093
NOTE_CS7 = 2217
NOTE_D7 = 2349
NOTE_DS7 = 2489
NOTE_E7 = 2637
NOTE_F7 = 2794
NOTE_FS7 = 2960
NOTE_G7 = 3136
NOTE_GS7 = 3322
NOTE_A7 = 3520
NOTE_AS7 = 3729
NOTE_B7 = 3951
NOTE_C8 = 4186
NOTE_CS8 = 4435
NOTE_D8 = 4699
NOTE_DS8 = 4978
DO4 = 262
DO4 = 262
RE4 = 294
MI4 = 330
FA4 = 349
FAS4 = 370
SOL4 = 392
LA4 = 440
LAS4 = 466
SI4 = 494
DO5 = 523
RE5 = 587
REST = 0

# Melodía de "We Wish You A Merry Christmas" con las variables de frecuencias
melodia_wish_you_merry_christmas = [
    (DO4, 400), (FA4, 400), (FA4, 400), (SOL4, 400), (FA4, 400), (MI4, 400), (RE4, 400), (RE4, 400),
    (RE4, 400), (SOL4, 400), (SOL4, 400), (LA4, 400), (SOL4, 400), (FA4, 400), (MI4, 400), (DO4, 400), (DO4, 400),
    (LA4, 400), (LA4, 400), (LAS4, 400), (LA4, 400), (SOL4, 400), (FA4, 400), (RE4, 400), (DO4, 400), (DO4, 400),
    (RE4, 400), (SOL4, 400), (MI4, 400), (FA4, 400), (DO4, 400), (FA4, 400), (FA4, 400), (FA4, 400),
    (MI4, 400), (MI4, 400), (FA4, 400), (MI4, 400), (RE4, 400), (DO4, 400), (SOL4, 400), (LA4, 400), (SOL4, 400),
    (SOL4, 400), (FA4, 400), (FA4, 400), (DO5, 400), (DO4, 400), (DO4, 400), (DO4, 400),
    (RE4, 400), (SOL4, 400), (MI4, 400), (FA4, 400)
]



# Ciclo infinito
while True:
    # Declaramos la variable para almacenar la distancia
    distancia = sensor.distance_cm()
    print("Distancia: ", distancia, " cm.")

    if distancia < 50:
        led.value(1)
        # Melodía 1n
        reproducir_melodia(melodia_wish_you_merry_christmas)
        sleep_ms(500)  # Pausa entre melodías
        
        # Verificar nuevamente la distancia antes de reproducir la siguiente melodía
        distancia = sensor.distance_cm()
        if distancia < 50:
            # Melodía 2
            led.value(1)
            reproducir_melodia(melodia_navidad_3)
            sleep_ms(500)  # Pausa entre melodías
            print("Distancia: en la 2 ", distancia, " cm.")
            
            # Verificar nuevamente la distancia antes de reproducir la siguiente melodía
            distancia = sensor.distance_cm()
            if distancia < 50:
                # Melodía 3
                led.value(1)
                reproducir_melodia(melodia_navidad_4)
                sleep_ms(500)  # Pausa entre melodías
                print("Distancia de la 3: ", distancia, " cm.")

       
    else:
        led.value(0)
        print("Distancia: ", distancia, " cm.")

    time.sleep(5)
