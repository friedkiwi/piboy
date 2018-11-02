
import RPi.GPIO as GPIO
import time

class LinkCable:
    mosiPin = 13
    misoPin = 19
    sclkPin = 26
    cable_clock = 8192


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

    def start(self):
        print "test"

    def handle_byte(self, byte):
        print "Received byte: %d" % (byte)

    def close(self):
        GPIO.cleanup()
