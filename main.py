import pygetwindow


def resize_and_move(window_title):
    sap_window = pygetwindow.getWindowsWithTitle(window_title)[0]
    sap_window.resizeTo(1300, 900)
    sap_window.moveTo(0, 0)
    sap_window.activate()


if __name__ == '__main__':
    resize_and_move('Super Auto Pets')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
