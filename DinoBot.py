from PIL import ImageGrab, ImageOps
import pyautogui
from time import sleep
from numpy import *


class Bot:

    dino = (335, 828) #top right pixel of dinosaur

    def jump(self):
        pyautogui.keyDown('space')
        sleep(0.1)
        pyautogui.keyUp('space')
        print('Jump')

    def check_box(self):
        #box which is checked constantly for obtacles
        box = (self.dino[0] + 60, self.dino[1], self.dino[0] + 100, self.dino[1] + 30)
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)

        a = array(grayImage.getcolors())
        return a.sum()


Game = Bot()
empty = 1447 #room without obstacles


def main():
    while True:
        if Game.check_box() != empty:
            Game.jump()


main()




