import psutil #libreria para ver el uso del CPU
from datetime import datetime
from gpiozero import LED
from time import sleep

#print(psutil.cpu_percent(interval = 1))
#print(psutil.cpu_count())

#Variables globales
led_yellow = LED(20)
led_red = LED(21)
file = open("/home/edgar/Desktop/cpu_usage_log.txt", "w")

while True:
    cpu_usage = psutil.cpu_percent(interval = 1, percpu= True)
    cpu_usage_mean = sum([i/len(cpu_usage) for i in cpu_usage])
    cpu_usage_mean = round(cpu_usage_mean, 3)
    print(f"cpu usage(%): {cpu_usage_mean}%")
    if 60 > cpu_usage_mean > 30:
        led_yellow.on()
        led_red.off()
    elif cpu_usage_mean >= 60:
        led_red.on()
        led_yellow.on()
    else:
        led_yellow.off()
        led_red.on()
    data = f"{datetime.now().strftime('%Y/%m/%d %HH %MM %SS')} " \
           f"cpu usage(%) : {cpu_usage_mean}% \n"
    file.write(data)
    sleep(1)
file.close()