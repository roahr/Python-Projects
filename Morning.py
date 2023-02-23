import time as t
import pywhatkit as messenger
import pyautogui as cur


def start_approval():
    while True:
        time=t.localtime()
        if time.tm_hour == 18 and time.tm_min == 30 and time.tm_sec == 00:
            return True
        


     
def sleep_sequence():
    with cur.hold("win"):
            cur.press("d")

    t.sleep(1)
    
    with cur.hold("alt"):
            with cur.hold("fn"):
                cur.press("f4")

    t.sleep(1)

    cur.press('up', presses=2)

    t.sleep(0.5)
    cur.press("enter")





if start_approval()==True:

        messenger.sendwhatmsg_instantly("+916374097176", "Good evening 😃")

        cur.press("enter")
        t.sleep(10)

        with cur.hold("ctrl"):
            cur.press("w")

        t.sleep(2)

        messenger.sendwhatmsg_instantly("+916374097176", "Looking great")

        cur.press("enter")
        t.sleep(10)

        with cur.hold("ctrl"):
            cur.press("w")
        
        t.sleep(2)

        sleep_sequence()


        

