from time import sleep
import RPi.GPIO as gpio
#GPIO.setmode(GPIO.BCM)
gpio.setwarnings(False)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(26, gpio.OUT)
    gpio.setup(19, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(6, gpio.OUT)

def turn_left(tf):
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(13, False)
    gpio.output(6, True)
    sleep(tf)
    
def turn_right(tf):
    gpio.output(26, True)
    gpio.output(19, False)
    gpio.output(13, True)
    gpio.output(6, False)
    sleep(tf)
    
def forward(tf):
    gpio.output(26, True)
    gpio.output(19, False)
    gpio.output(13, False)
    gpio.output(6, True)
    sleep(tf)
    
def reverse(tf):
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(13, True)
    gpio.output(6, False)
    sleep(tf)

def stop(tf):
    gpio.output(26, False)
    gpio.output(19, False)
    gpio.output(13, False)
    gpio.output(6, False)
    sleep(tf)
    gpio.cleanup()
    
def drive(direction, tym):
    init()
    
    if direction == "forward":
        forward(tym)
        stop(tym)
        
    elif direction == "reverse":
        reverse(tym)
        stop(tym)

    elif direction == "left":
        turn_left(tym)
        stop(tym)

    elif direction == "right":
        turn_right(tym)
        stop(tym)

    elif direction == "stop":
        stop(tym)

    else :
        stop(tym)



if __name__ == '__main__':
	import sys
	drive((sys.argv[1]), float(sys.argv[2]))
	gpio.cleanup()

##
##init()
##forward(0.6)
##sleep(1)
##reverse(0.6)
##sleep(1)
##turn_right(0.6)
##sleep(1)
##turn_left(0.6)
##stop(1)
