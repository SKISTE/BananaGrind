import win32gui
import win32api
import win32con
import pyautogui
import random
import subprocess
import psutil
import os
from progress.bar import Bar
from time import sleep

def open_exe(file_path):
    process = subprocess.Popen(file_path)
    return process.pid

def close_exe_by_name(exe_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == exe_name:
            process.terminate()
            break

def get_application_center(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        center_x = (rect[0] + rect[2]) // 2
        center_y = (rect[1] + rect[3]) // 2
        return (center_x, center_y)
    return None

def click_times(num,coords):
    for x in range(0,num):
        pyautogui.click(coords[0],coords[1])

def sleep_progress(secs):
    bar = Bar('Сплю', max=secs)
    for x in range(0,secs):
        bar.next()
        sleep(1)
    bar.finish()
        

# Пример использования:


PATH = open('path.txt','r').read()

# close_exe_by_name('Banana.exe')


while True:
    print('Открываю exe')
    
    pid = open_exe(PATH)

    print('Сплю 13 секунд')
    sleep_progress(13)

    rnd = random.randint(30,50)
    print('Нахожу центр и кликаю '+str(rnd)+' раз')
    center = get_application_center("Banana")
    click_times(rnd,center)

    print('Сплю 3600 секунд')
    sleep_progress(3600)

    print('Закрываю банан')
    close_exe_by_name('Banana.exe')

    print('Сплю 4 секунды')
    sleep_progress(4)
    print('Конец цикла\n=====\n\n\n\n')
    



print('ff') 