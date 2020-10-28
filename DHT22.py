import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    umid, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    if umid is not None and temp is not None:
        print("Temperatura = {0:0.1f}*C  Umidade = {1:0.1f}%".format(temp, umid))
    else:
        print("Falha ao ler os dados do sensor")