from gpiozero import DistanceSensor, LED
from time import sleep

# Definir pines GPIO para el sensor ultrasónico y LEDs
sensor_pin = 18  # Cambia este pin según tu configuración
led_red_pin = 17
led_amber_pin = 27
led_green_pin = 22

# Crear objetos DistanceSensor y LED
sensor = DistanceSensor(echo=sensor_pin, trigger=sensor_pin, threshold_distance=1)
led_red = LED(led_red_pin)
led_amber = LED(led_amber_pin)
led_green = LED(led_green_pin)

try:
    while True:
        # Medir la distancia en decímetros
        distance_cm = sensor.distance * 100  # Convertir de metros a centímetros
        distance_dm = distance_cm / 10  # Convertir de centímetros a decímetros

        # Encender el LED correspondiente al rango de distancia
        if distance_dm < 20:
            led_red.on()
            led_amber.off()
            led_green.off()
        elif distance_dm > 80:
            led_red.off()
            led_amber.off()
            led_green.on()
        else:
            led_red.off()
            led_amber.on()
            led_green.off()

        sleep(0.1)  # Esperar un breve período antes de la próxima medición

except KeyboardInterrupt:
    # Limpiar los pines GPIO al salir
    led_red.off()
    led_amber.off()
    led_green.off()
