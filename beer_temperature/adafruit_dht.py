import importlib.util

adafruit_spec = importlib.util.find_spec("Adafruit_DHT")
found = adafruit_spec is not None

if found:
    adafruit = importlib.util.module_from_spec(adafruit_spec)
    adafruit_spec.loader.exec_module(adafruit)


def read():
    if found:
        return adafruit.read_retry(11, 4)
    else:
        return { 77, 7 }
