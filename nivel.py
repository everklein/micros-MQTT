import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 16 #Trigger conectado no pino fisico 16
      PIN_ECHO = 18 #Echo conectado no pino fisico 18

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      time.sleep(2) # aguarda 2 seg para estabilizar o sensor

      GPIO.output(PIN_TRIGGER, GPIO.HIGH) #pulso nivel alto

      time.sleep(0.00001) #pausa por 1n seg

      GPIO.output(PIN_TRIGGER, GPIO.LOW) #pulso nivel baixo
#lendo os tempos para calcular a duração da onda
      while GPIO.input(PIN_ECHO)==0: #verifica se echo esta baixo
            pulse_start_time = time.time() #tempo atual
      while GPIO.input(PIN_ECHO)==1: #verifica se esta alto
            pulse_end_time = time.time() #tempo atual
            
#calculando a distancia: vel som é 34300 cm/s. Queremos so a distancia da ida da onda, então
#34300 cm/s /2 = 17150 cm/s
      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print ("Distance:",distance,"cm")

finally:
      GPIO.cleanup() #fim do try e limpa script





