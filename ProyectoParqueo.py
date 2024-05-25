import time
import board
import busio
import adafruit_ahtx0
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import RPi.GPIO as GPIO

# Configurar la comunicación I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Crear el objeto del sensor AHT10
sensor = adafruit_ahtx0.AHTx0(i2c)

# Configuración de la pantalla LCD
lcd_columns = 16
lcd_rows = 2

# Configuración de pines para la pantalla LCD
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D11)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D14)
lcd_d7 = digitalio.DigitalInOut(board.D8)

# Inicializar la pantalla LCD
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Configuración del botón y LED
buttonPin = 9  # Pin GPIO 9 para el botón
ledPin = 25    # Pin GPIO 25 para el LED

# Configuración de los pines GPIO adicionales
button_up = 4  # Pin para el botón que incrementa el contador
button_down = 5  # Pin para el botón que decrementa el contador
servo_pin = 19  # Pin para el servo motor
button_pins = [10, 16, 13,  6]  # Pines para botones adicionales

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo_pin, GPIO.OUT)
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configuración del servo motor
servo = GPIO.PWM(servo_pin, 50)  # Frecuencia de 50Hz
servo.start(0)

# Definir los pines del motor DC
DC_IN1 = 17  # Pin GPIO para IN1 del motor
DC_IN2 = 22  # Pin GPIO para IN2 del motor
DC_ENABLE = 18  # Pin GPIO para ENABLE del motor

GPIO.setup(DC_IN1, GPIO.OUT)
GPIO.setup(DC_IN2, GPIO.OUT)
GPIO.setup(DC_ENABLE, GPIO.OUT)

# Inicialmente, el motor está apagado
GPIO.output(DC_ENABLE, GPIO.LOW)

# Definir los pines del motor paso a paso
IN1 = 1  # GPIO 1
IN2 = 27  # GPIO 27
IN3 = 21  # GPIO 21
IN4 = 12  # GPIO 12

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Definir la secuencia de pasos del motor paso a paso
sequence = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
]

# Variables de estado
count = 0
decrements = 0

def set_servo_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    servo.ChangeDutyCycle(0)

def move_servo():
    set_servo_angle(120)  # Mover el servo motor a 120 grados
    time.sleep(1)
    set_servo_angle(20)  # Volver el servo motor a 20 grados

def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)

def giro90(delay):
    for i in range(52):  # Gira 90 grados
        for step in sequence:
            setStep(step[0], step[1], step[2], step[3])
            time.sleep(delay)

def regreso90(delay):
    for i in range(52):  # Gira de regreso 90 grados
        for step in reversed(sequence):
            setStep(step[0], step[1], step[2], step[3])
            time.sleep(delay)

def motor_forward():
    GPIO.output(DC_IN1, GPIO.HIGH)
    GPIO.output(DC_IN2, GPIO.LOW)

def motor_stop():
    GPIO.output(DC_IN1, GPIO.LOW)
    GPIO.output(DC_IN2, GPIO.LOW)

try:
    while True:
        # Leer la temperatura
        temperature = sensor.temperature
        temp_str = f"T:{temperature:.2f}"

        # Leer el estado del botón
        buttonState = GPIO.input(buttonPin)
        if buttonState == GPIO.HIGH:
            GPIO.output(ledPin, GPIO.HIGH)
            button_status = "I:A"
        else:
            GPIO.output(ledPin, GPIO.LOW)
            button_status = "I:D"

        # Contar el número de botones activos
        active_buttons = 0
        for pin in button_pins:
            if GPIO.input(pin) == GPIO.LOW:  # El botón está presionado
                active_buttons += 1

        # Manejar los botones up y down
        if GPIO.input(button_up) == GPIO.LOW:
            if count < 4:
                count += 1
                print(f"Count: {count}")
                move_servo()
                time.sleep(0.2)  # Debounce delay

        if GPIO.input(button_down) == GPIO.LOW:
            if count > 0:
                count -= 1
                decrements += 1
                print(f"Count: {count}")
                giro90(0.01)  # Gira 90 grados
                time.sleep(1)  # Pausa de 1 segundo
                regreso90(0.01)  # Gira de regreso 90 grados
                time.sleep(1)  # Evita múltiples activaciones rápidas
                time.sleep(0.2)  # Debounce delay

        # Encender o apagar el motor DC basado en la temperatura
        if temperature > 24:
            GPIO.output(DC_ENABLE, GPIO.HIGH)
            motor_status = "V:E"
        else:
            GPIO.output(DC_ENABLE, GPIO.LOW)
            motor_status = "V:A"

        # Actualizar la primera línea de la LCD con la temperatura y el estado del botón
        lcd_line1 = f"{temp_str} {button_status} ECCI"
        # Actualizar la segunda línea de la LCD con el número de botones activos, el valor de count, el número de decrementos y el estado del motor
        lcd_line2 = f"PA:{active_buttons} E:{count} S:{decrements} {motor_status}"
        lcd.message = f"{lcd_line1}\n{lcd_line2}"

        # Esperar 1 segundo antes de la siguiente lectura
        time.sleep(1)

except KeyboardInterrupt:
    # Limpiar la pantalla LCD y los pines GPIO al interrumpir el programa
    lcd.clear()
    GPIO.cleanup()
    servo.stop()
