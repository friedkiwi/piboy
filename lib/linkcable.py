
import RPi.GPIO as GPIO
import time

class LinkCable:
    mosiPin = 13
    misoPin = 19
    sclkPin = 26
    cable_clock = 8192
    
    shift = 0
    out_data = 0
    in_data = 0


    def open(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.mosiPin, GPIO.OUT)
        GPIO.setup(self.misoPin, GPIO.IN)
        GPIO.setup(self.sclkPin, GPIO.IN)

    def get_clock_interval(self):
        return (1 / self.cable_clock)

    def get_sclk(self):
        return GPIO.input(self.sclkPin)

    def has_clock(self):
        pulses_detected = 0
        for x in range(0, self.cable_clock * 2):
            if self.get_sclk():
                pulses_detected += 1
            time.sleep(self.get_clock_interval() / 2)
        return pulses_detected > 25

    def wait_sclk_on(self):
        while not GPIO.input(self.sclkPin):
            time.sleep(self.get_clock_interval() / 64)

    def wait_sclk_off(self):
        while GPIO.input(self.sclkPin):
            time.sleep(self.get_clock_interval() / 64)

    def start(self):
        shift = 0
        out_data = 0
        while True:
            self.wait_sclk_off()
            self.in_data |= int(GPIO.input(self.mosiPin)) << (7 - shift)
            shift += 1

            if shift > 7:
                shift = 0
                out_data = self.handle_byte(self.in_data)
                out_data = out_data & 0xFF
                in_data = 0
            
            self.wait_sclk_on()
            GPIO.output(self.mosiPin, (out_data & 0x80) == 1)
            out_data <<= 1


    def handle_byte(self, byte):
        print "Received byte: %d" % (byte)
        return byte

    def close(self):
        GPIO.cleanup()
