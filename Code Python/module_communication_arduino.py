class Arduino:
    import serial
    import time
    def __init__(self, port, baudrate=9600):
        self.baudrate = baudrate
        self.dev = self.serial.Serial(port, baudrate=baudrate)

    def envoi_message_et_recoit_reponse(self, message):
        self.dev.write(message.encode('ascii'))
        self.time.sleep(500/self.baudrate) # délai pour s'assurer que l'Arduino ait le temps de transmettre la valeur via le port série ; 500/baudrate est empirique
        line = self.dev.readline().decode('ascii').strip()
        return line