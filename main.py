from ili934xnew import ILI9341, color565
import machine
from machine import Pin, SPI, PWM
from micropython import const
import time
import os
import glcdfont
import tt14
import tt24
import tt32
import time

#crvena 3.3, smedja masa, narandzasta PWM 2000-5000 duty


# Dimenzije displeja
SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(2)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)

# Podešenja SPI komunikacije sa displejem
TFT_CLK_PIN = const(18)
TFT_MOSI_PIN = const(19)
TFT_MISO_PIN = const(16)
TFT_CS_PIN = const(17)
TFT_RST_PIN = const(20)
TFT_DC_PIN = const(15)

# Fontovi na raspolaganju
fonts = [glcdfont,tt14,tt24,tt32]

spi = SPI(
    0,
    baudrate=1002500000,
    miso=Pin(TFT_MISO_PIN),
    mosi=Pin(TFT_MOSI_PIN),
    sck=Pin(TFT_CLK_PIN))

display = ILI9341(
    spi,
    cs=Pin(TFT_CS_PIN),
    dc=Pin(TFT_DC_PIN),
    rst=Pin(TFT_RST_PIN),
    w=SCR_WIDTH,
    h=SCR_HEIGHT,
    r=SCR_ROT)

display.set_font(tt32)


def prikaziPocetniDisplej():
    display.erase()
    # Različita orijentacija teksta na displeju
    display.set_pos(45,30)
    display.rotation=0
    display.print('Unesite PIN:')

    display.set_pos(70,100)
    display.print('_ _ _ _')

    # Offset za prikaz slike
    offset_x = 160
    offset_y = 0


    # Učitavanje slike iz BMP fajla
    f=open('macka3.bmp', 'rb')

    # Prikaz piksela slike na displeju
    if f.read(2) == b'BM':  #header
        dummy = f.read(8) #file size(4), creator bytes(4)
        offset = int.from_bytes(f.read(4), 'little')
        hdrsize = int.from_bytes(f.read(4), 'little')
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
            depth = int.from_bytes(f.read(2), 'little')
            if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
                print("Image size:", width, "x", height)
                rowsize = (width * 3 + 3) & ~3
                if height < 0:
                    height = -height
                    flip = False
                else:
                    flip = True
                w, h = width, height
                for row in range(h):
                    if flip:
                        pos = offset + (height - 1 - row) * rowsize
                    else:
                        pos = offset + row * rowsize
                    if f.tell() != pos:
                        dummy = f.seek(pos)
                    for col in range(w):
                        bgr = f.read(3)
                        display.pixel(offset_y+col,offset_x+row,color565(bgr[2],bgr[1],bgr[0]))


def prikaziDisplejZaTacanPin():
    print("Tacan")
    display.erase()
    display.set_pos(35,20)
    display.rotation=0
    display.print('Ispravan PIN')
    userPIN = ""
           
    # Offset za prikaz slike
    offset_x = 65
    offset_y = 30

    # Učitavanje slike iz BMP fajla
    f=open('tacan(2).bmp', 'rb')

    # Prikaz piksela slike na displeju
    if f.read(2) == b'BM':  #header
        dummy = f.read(8) #file size(4), creator bytes(4)
        offset = int.from_bytes(f.read(4), 'little')
        hdrsize = int.from_bytes(f.read(4), 'little')
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
            depth = int.from_bytes(f.read(2), 'little')
            if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
                rowsize = (width * 3 + 3) & ~3
                if height < 0:
                    height = -height
                    flip = False
                else:
                    flip = True
                w, h = width, height
                for row in range(h):
                    if flip:
                        pos = offset + (height - 1 - row) * rowsize
                    else:
                        pos = offset + row * rowsize
                    if f.tell() != pos:
                        dummy = f.seek(pos)
                    for col in range(w):
                        bgr = f.read(3)
                        display.pixel(offset_y+col,offset_x+row,color565(bgr[2],bgr[1],bgr[0]))
     

def prikaziDisplejZaNetacanPin():
    print("Netacan")
    userPIN = ""
    wrongPinCounter = 0
    display.erase()
    display.set_pos(25,20)
    display.rotation=0
    display.print('Neispravan PIN')
    userPIN = ""
    # Offset za prikaz slike
    offset_x = 85
    offset_y = 25

    # Učitavanje slike iz BMP fajla
    f=open('neee.bmp', 'rb')

    # Prikaz piksela slike na displeju
    if f.read(2) == b'BM':  #header
        dummy = f.read(8) #file size(4), creator bytes(4)
        offset = int.from_bytes(f.read(4), 'little')
        hdrsize = int.from_bytes(f.read(4), 'little')
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
            depth = int.from_bytes(f.read(2), 'little')
            if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
                rowsize = (width * 3 + 3) & ~3
                if height < 0:
                    height = -height
                    flip = False
                else:
                    flip = True
                w, h = width, height
                for row in range(h):
                    if flip:
                        pos = offset + (height - 1 - row) * rowsize
                    else:
                        pos = offset + row * rowsize
                    if f.tell() != pos:
                        dummy = f.seek(pos)
                    for col in range(w):
                        bgr = f.read(3)
                        display.pixel(offset_y+col,offset_x+row,color565(bgr[2],bgr[1],bgr[0]))
    prikaziPocetniDisplej()
     
prikaziPocetniDisplej()

R1 = Pin(21, Pin.OUT)
R2 = Pin(22, Pin.OUT)
R3 = Pin(26, Pin.OUT)
R4 = Pin(27, Pin.OUT)
C1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
C2 = Pin(1, Pin.IN, Pin.PULL_DOWN)
C3 = Pin(2, Pin.IN, Pin.PULL_DOWN)
C4 = Pin(3, Pin.IN, Pin.PULL_DOWN)

row = [R1, R2, R3, R4]
column = [C1, C2, C3, C4]

counter = 0

for i in range(0,4):
    row[i].value(0)

counter = 0
isPressed = False
autoIncrement = False
autoTimer = 0.

keyMatrix = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]]

correctPIN = 2306
userPIN = ""
wrongPinCounter = 0
isKey = False
secondCounter = 0

def getPressedKey(rows, columns):
    global isKey
    for i in range(0,4):
        rows[i].value(1)
        for j in range(0,3):
            if columns[j].value() == 1 and isKey == False:
                rows[i].value(0)
                isKey = True
                return keyMatrix[i][j]
        rows[i].value(0)
       
varijabla=43
brojac=0

while 1:
    key = getPressedKey(row, column)
    if key != None and key != "#":
        if key != "*" and brojac<4:
            varijabla=varijabla+32
            display.set_pos(varijabla,90)
            display.set_color(color565(255, 255, 255), color565(0, 0, 0))
            display.print(key)
        else:
            brojac = brojac - 1
            display.set_pos(varijabla,90)
            display.set_color(color565(0, 0, 0), color565(0, 0, 0))
            display.print("■")
            varijabla=varijabla-32
    if key != None and key != "*" and key != "#":
        if len(userPIN) < 4:
            userPIN = userPIN + key
            brojac = brojac + 1
    elif key == "*" and len(userPIN)>0:
        userPIN = userPIN[:-1]
       
    elif key == "#":
        if len(userPIN) < 4 or int(userPIN) != correctPIN:
            prikaziDisplejZaNetacanPin()
        else:
            prikaziDisplejZaTacanPin()
    else:
        isKey = False
    print(userPIN)
    res = [int(x) for x in str(userPIN)]
    while len(res) < 4:
        res.insert(0,0)
    for i in range(0,4):
        time.sleep(0.05)
