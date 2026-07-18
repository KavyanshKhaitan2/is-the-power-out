import machine
from machine import ADC, Pin
import time
import network
import urequests

wifi_ssid = '<WIFI_SSID>'
wifi_pass = '<WIFI_PASSWORD>'

led = Pin(21, Pin.OUT)
led.off()
outlet_detect = ADC(Pin(26))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
    print('Waiting for connection...')
    led.toggle()
    sleep(0.1)
led.off()
time.sleep(2)

has_power = None
status = None
while True:
    voltage = outlet_detect.read_u16() * (3.3 / 65535)
    if voltage > 1.5:
        led.on()
        if has_power is True:
            continue
        has_power = True
        status = ":online:"
    else:
        led.off()
        if has_power is False:
            continue
        has_power = False
        status = ":offline:"
    if status:
        print("Attempting to update Slack status")
        r = urequests.post("<SLACK_WEBHOOK_URL>", data={
            "message": "Current status: "+status
        })
        status = None
    time.sleep(2)
