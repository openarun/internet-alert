import requests
import socket
from gi.repository import Notify
import vlc
import time
p = vlc.MediaPlayer("ambulance_alarm.mp3")


def check_internet(host="8.8.8.8", port=53, timeout=5):
    try:

        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        print(ex)
        return False

def notify_box(msg):
    # One time initialization of libnotify
    Notify.init(msg)

    # Create the notification object
    summary = msg
    body = msg
    notification = Notify.Notification.new(
        summary,
        body, # Optional
    )
    # Actually show on screen
    notification.show()

def play_siren():
    p.play()

def stop_siren():
    p.stop()

try:
    connected = False

    while(True):
        if check_internet():
            print("internet is aayo")
            connected = True
            notify_box("Internet Aayo !!")
            play_siren()
            time.sleep(1)
        else:
            print("internet is down")
            stop_siren()
except KeyboardInterrupt:
    print("Keyboard Exiting...")


        
 
