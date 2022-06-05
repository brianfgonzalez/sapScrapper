import pygetwindow
import cv2 as cv
import numpy as np
import os
from PIL import ImageGrab
import time


def resize_and_move(window_title):
    window = pygetwindow.getWindowsWithTitle(window_title)[0]
    window.resizeTo(1300, 900)
    window.moveTo(0, 0)
    window.activate()
    return window


def click_on_button(ui_img, button_image):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    button_img = cv.imread('images/buttons/' + button_image, cv.IMREAD_UNCHANGED)
    cv.imshow('color image', cv.img_color)
    result = cv.matchTemplate(ui_img, button_img, cv.TM_CCOEFF)
    # I've inverted the threshold and where comparison to work with TM_SQDIFF_NORMED
    threshold = 0.99
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))
    return locations


if __name__ == '__main__':
    sap_window = resize_and_move('Super Auto Pets')
    # click_on_button('arena_mode.JPG')
    time.sleep(1)
    # print(sap_window.area)
    sap_window_img = np.array(ImageGrab.grab(sap_window.box).convert('RGB'))
    print(click_on_button(sap_window_img, 'arena_mode.JPG'))
