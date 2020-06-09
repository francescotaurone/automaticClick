import pyautogui
import time


def clickForMe(nextX, nextY, secToWait):
    try:
        while True:
            x, y = pyautogui.position()
            pyautogui.moveTo(nextX, nextY)
            pyautogui.click()
            pyautogui.moveTo(x, y)
            print("Click!")
            
            time.sleep(secToWait)

    except KeyboardInterrupt:
        print('\n')

def getCoordToClick():
    input("Position the cursor on the position to click and press enter...")
    
    x, y = pyautogui.position()
    print("Saved position: {}, {}".format(x, y))
    while(True):
        secToWait = input("Write the number of seconds to wait between each click:\n")
        secToWait = float(secToWait)
        if type(secToWait) != float:
            print("The number you inserted is not valid, try again!\n")
        else:
            break
    return x, y, secToWait

if __name__ == "__main__":
    nextX, nextY, secToWait = getCoordToClick()
    input("Whenever you want to start, press enter. To terminate, press ctrl+c")
    clickForMe(nextX, nextY, secToWait)