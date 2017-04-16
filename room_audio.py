import RPi.GPIO as GPIO
import time
from pygame import mixer
import sys

sound_dir = "/home/pi/Developer/barnyard-audio/sounds/"
mixer.init()

def main(room_num):
    room_audio = mixer.Sound(sound_dir + 'Room_'+room_num+'.wav')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    main_channel = mixer.Channel(0)

    while True:
        time.sleep(0.05)

        if GPIO.input(22) and not main_channel.get_busy():
    	    main_channel.play(room_audio) 

if __name__ == "__main__":
    main(sys.argv[1])
