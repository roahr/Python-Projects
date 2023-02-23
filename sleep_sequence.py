import time as t
import pyautogui as cur

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

sleep_sequence()



            
