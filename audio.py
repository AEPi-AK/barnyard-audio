from time import sleep
from pygame import mixer
import json
import urllib2

# Conditions we check for
# Game State:
#   Player 1 unjoin -> join         Join sound 1
#   Player 2 unjoin -> join         Join sound 2
#   Game Waiting Phase              Something neutral
#   Game joining                    get pumped sound

# We hae up to 8 channels, so we split up the channels as follows
# Channel 1 -> phase sounds (including join, waiting sounds)
#           -> world sounds (dessert, etc.)
# Channel 2 -> Dialogue
#           -> Player joining

addr = "http://localhost:3000"

def phaseSound(phase, channel):
    if phase == "GameWaiting":
        #channel.play(SOUND, loops=-1, fade_ms=500)
    elif phase == "GameJoining":
        #channel.play(SOUND, loops=-1, fade_ms=500)
    elif phase == "Desert":
        #channel.play(SOUND, loops=-1, fade_ms=500)
    elif phase == "Tundra":
        #channel.play(SOUND, loops=-1, fade_ms=500)
    elif phase == "WinnerPlayer1":
        #channel.play(SOUND, loops=-1, fade_ms=500)
    elif phase == "WinnerPlayer2":
        #channel.play(SOUND, loops=-1, fade_ms=500)

def player1Sound(channel):
    #channel.play(SOUND, loops=-1, fade_ms=500)

def player2Sound(channel):
    #channel.play(SOUND, loops=-1, fade_ms=500)


def main(argv):
    # Set up sounds
    volume = 0.5
    mixer.init()
    main_channel = mixer.Channel(0)
    supp_channel = mixer.Channel(1)

    # Default JSON
    prev_formatted = json.loads('{"phaseTime":"0","player1":{"slot0":"NoHead","slot1":"NoBody",' \
        + '"joined":"False","slot2":"NoLeg"},"location":"Desert","settings":{"volume":"50","bri' \
        + 'ghtness":"255"},"currentPhase":"GameWaiting","timeSincePhaseStart":"442410.579593","' \
        + 'player2":{"slot0":"NoHead","slot1":"NoBody","joined":"False","slot2":"NoLeg"},"winne' \
        + 'r":"Player1"}')

    while True:
        req_raw = urllib2.urlopen(addr + "/gamestate")
        req_formatted = json.loads(req_raw)

        prev_vol = volume
        volume = (req_formatted["settings"]["volume"]/100.0)
        if volume != prev_volume:
            main_channel.set_volume(volume)
            supp_channel.set_volume(volume)

        if req_formatted["currentPhase"] != prev_formatted["currentPhase"] or \
                req_formatted["location"] != prev_formatted["location"] :
            # Phase Change, play appropriate sound
            current_phase = req_formatted["currentPhase"]
            if current_phase == "GameInProgress":
                current_phase = req_formatted["location"]
            elif current_phase = "GameOver":
                current_phase = "Winner" + req_formatted["winner"]

            phaseSound(current_phase, main_channel)

        if !prev_formatted["player1"]["joined"] and req_formatted["player1"]["joined"]:
            # Player 1 has joined
            player1Sound(supp_channel)

        if !prev_formatted["player2"]["joined"] and req_formatted["player2"]["joined"]:
            # Player 2 has joined
            player2Sound(supp_channel)

        prev_formatted = req_formatted
        sleep(0.05)

if __name__ == "__main__":
    main(sys.argv[1:])
