import pyautogui as pg
from time import sleep

serc = pg.locateOnScreen
tik = pg.click
sleep(3)
while True:
    if serc("bekle.png", confidence=0.95) != None:
        print("bekle var")
        pg.moveTo(1166, 588)
        sleep(0.3)
        pg.moveTo(1156, 588)
        sleep(0.3)
        pg.moveTo(1156, 598)
        sleep(0.3)
        pg.moveTo(1166, 598)
        sleep(0.3)
        if serc("ses.png", confidence=0.95) != None:
            print("tıkladım sese")
            tik(serc("ses.png", confidence=0.95))
        if serc("ok.png", confidence=0.95) != None:
            print("ok var")
            tik(serc("ok.png", confidence=0.95))
        sleep(1)
    else:
        if serc("yenii.png", confidence=0.9) != None:
            print("yeniye tıklicam")
            tik(serc("yenii.png", confidence=0.9))
            sleep(4)
            tik(1166, 588)
            print("vid baslio")
        else:
            print("aşağı indiriom")
            tik(468, 1018)
            sleep(1)
    sleep(2)
