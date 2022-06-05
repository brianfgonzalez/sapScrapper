import pygetwindow
import cv2
import numpy
import os
from PIL import ImageGrab, Image
import time


def resize_and_move(window_title):
    window = pygetwindow.getWindowsWithTitle(window_title)[0]
    window.resizeTo(1300, 900)
    window.moveTo(0, 0)
    window.activate()
    return window


def click_on_button(img, button_image):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # button_img = cv2.imread('images/buttons/' + button_image, cv2.IMREAD_UNCHANGED)
    tamplate = cv2.cvtColor(numpy.array(Image.open('images/buttons/' + button_image)), cv2.COLOR_RGB2BGR)
    # RGB_img = cv2.cvtColor(ui, cv.COLOR_BGR2GRAY)
    # cv2.imshow('ui window', button_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    res = cv2.matchTemplate(img, button_image, cv2.TM_CCOEFF_NORMED)
    # I've inverted the threshold and where comparison to work with TM_SQDIFF_NORMED
    # threshold = 0.75
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    # locations = numpy.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    # locations = list(zip(*locations[::-1]))

    # all matches:
    threshold = 0.75
    loc = numpy.where(res >= threshold)
    found = 0
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 220), 1)
        found += 1

    # best match:
    best = numpy.amax(res)
    pt = numpy.where(res == best)[::-1]
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    print('Found: {}\nBest: {}'.format(found, best));

    Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).show()

    # return locations


if __name__ == '__main__':
    sap_window = resize_and_move('Super Auto Pets')
    # click_on_button('arena_mode.JPG')
    time.sleep(1)
    # print(sap_window.area)
    #sap_window_img = np.array(ImageGrab.grab(sap_window.box))
    # sap_window_img = np.array(ImageGrab.grab(sap_window.box))

    sap_window_img = cv2.cvtColor(numpy.array(ImageGrab.grab(sap_window.box)), cv2.COLOR_RGB2BGR)
    click_on_button(sap_window_img, 'arena_mode.JPG')
