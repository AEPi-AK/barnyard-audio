import RPi.GPIO as GPIO
import time
from pygame import mixer

sound_dir = "sounds/"
mixer.init()
example = mixer.Sound(sound_dir + 'room_0.wav')

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    main_channel = mixer.Channel(0)

    while True:
        time.sleep(0.05)

        if GPIO.input(22) and not main_channel.get_busy():
            print("playing audio?")
    	    main_channel.play(example) 

if __name__ == "__main__":
    main()
