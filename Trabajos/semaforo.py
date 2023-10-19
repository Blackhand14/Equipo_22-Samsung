from gpiozero import LED, Button
from time import sleep

# Definir pines GPIO para LEDs y botón
led_pins = [17, 18, 27]  # Cambia estos pines según tu configuración
button_pin = 22  # Cambia este pin según tu configuración

# Crear objetos LED y Button
leds = [LED(pin) for pin in led_pins]
button = Button(button_pin)

# Estado inicial
current_led_index = 0

# Función para cambiar al siguiente LED
def next_led():
    global current_led_index
    leds[current_led_index].off()
    current_led_index = (current_led_index + 1) % len(leds)
    leds[current_led_index].on()

# Configurar evento de clic de botón
button.when_pressed = next_led

try:
    # Encender el primer LED al inicio
    leds[current_led_index].on()

    # Mantener el programa en ejecución
    while True:
        sleep(0.1)  # Evitar el uso excesivo de la CPU

except KeyboardInterrupt:
    # Limpiar los pines GPIO al salir
    for led in leds:
        led.off()
