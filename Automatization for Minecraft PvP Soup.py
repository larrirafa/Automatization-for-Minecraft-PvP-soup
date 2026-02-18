import pyautogui as pa
import time
import keyboard

pa.PAUSE = 0.024

def remouse():
    # Open inventory
    pa.press("e")
    time.sleep(0.08) # Timer to prevent bugs

    pa.moveTo(x=961, y=573) # Start automatization
    pa.rightClick()
    pa.moveTo(x=990, y=415)
    pa.leftClick()

    #Clicking on mushroom

    pa.moveTo(x=1042, y=567)
    pa.rightClick()
    pa.moveTo(x=1075, y=430)
    pa.leftClick()

    #Clicking on mushroom two

    pa.moveTo(x=1103, y=575)
    pa.rightClick()
    pa.moveTo(x=1067, y=342)
    pa.leftClick()

    #Pulling recraft

    pa.moveTo(x=1212, y=382) #Pointer for recraft box
    with pa.hold('shift'):
        pa.click()

        pa.moveTo(x=1067, y=342)# Pulling recraft
        pa.click()

        
        pa.moveTo(x=1075, y=430)# Pulling recraft two
        pa.click()

        
        pa.moveTo(x=990, y=415) # Pulling pot
        pa.click()

        pa.press("e") # Close Inventory
        pa.rightClick() # Eating soup


print("Press R to start e HOME to leave")

keyboard.add_hotkey("r", remouse)
keyboard.wait("home")