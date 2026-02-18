import pyautogui as pa
import time
import keyboard

pa.PAUSE = 0.024
def remouse():
    
    pa.press("e")

    time.sleep(0.08)
    pa.moveTo(x=964, y=580, duration=0)
    pa.rightClick()
    pa.moveTo(x=976, y=502, duration=0)
    pa.leftClick()

    

    pa.moveTo(x=1000, y=584, duration=0)
    pa.rightClick()
    pa.moveTo(x=1011, y=506, duration=0)
    pa.leftClick()

    

    pa.moveTo(x=1034, y=586, duration=0)
    pa.rightClick()
    pa.moveTo(x=1013, y=467, duration=0)
    pa.leftClick()

    

    pa.moveTo(x=1088, y=495, duration=0)
    with pa.hold('shift'):
        pa.click()

        pa.moveTo(x=1013, y=467, duration=0)
        pa.click()

        pa.moveTo(x=1011, y=506, duration=0)
        pa.click()

        pa.moveTo(x=976, y=502, duration=0)
        pa.click()

        pa.press("e")
        pa.tripleClick(button="right")
        pa.tripleClick(button="right")

print("Pronto aperte R para executar e ESC para sair  ")

keyboard.add_hotkey("r", remouse)
keyboard.wait("esc")