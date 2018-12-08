#!/usr/bin/python
import sys
import threading
import Adafruit_DHT
import ConfigParser

config = ConfigParser.RawConfigParser()
config.add_section('Temperature')
config.add_section('Humidity')

t_count = 0
t_avrg = 0
t_min = 100
t_max = 0
t_last = 0

def printIt():
    threading.Timer(60.0, printIt).start()

    h, t = Adafruit_DHT.read_retry(11, 4)

    global t_avrg, t_count, t_min, t_max

    t_avrg = t_avrg * t_count + t
    t_count = t_count + 1
    t_avrg = t_avrg / t_count

    if t_min > t:
        t_min = t

    if t_max < t:
        t_max = t

    config.set('Temperature', 'count', t_count)
    config.set('Temperature', 'average', t_avrg)
    config.set('Temperature', 'min', t_min)
    config.set('Temperature', 'max', t_max)

    with open('/home/pi/Desktop/temp.cfg', 'wb') as configFile:
        config.write(configFile)

printIt()
