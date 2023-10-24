import psutil #libreria para ver el uso de la ras
from datetime import datetime
from gpiozero import LED
from time import sleep

#print(psutil.cpu_percent(interval = 1))
#print(psutil.cpu_count())

#Variables globales
led_yellow = LED(20)
led_red = LED(21)
file = open("/home/edgar/Desktop/disk_usage_log.txt", "w")

while True:
    disk_usage = psutil.disk_partitions()
    disk_usage_mean = psutil.disk_usage("/").percent
    #disk_usage_mean = round(disk_usage_mean, 3)
    print(f"disk usage(%): {disk_usage_mean}%")
    if 60 > disk_usage_mean > 30:
        led_yellow.on()
        led_red.off()
    elif disk_usage_mean >= 60:
        led_red.on()
        led_yellow.on()
    else:
        led_yellow.off()
        led_red.off()
    data = f"{datetime.now().strftime('%Y/%m/%d %HH %MM %SS')} " \
           f"disk usage(%) : {disk_usage_mean}% \n"
    file.write(data)
    sleep(1)
file.close()
