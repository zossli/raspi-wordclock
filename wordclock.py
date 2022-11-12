import random
import sys
import time
from datetime import datetime, timedelta

import board
import neopixel

from still import Still
from wordlist import *
from words import Word

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_rows = 12
num_columns = 12
num_pixels = num_rows * num_columns
i = 0

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.10, auto_write=False, pixel_order=ORDER
)

pixels.fill((0,0,0))

def getPixelNr(x,y):
    return ((y-1)*12+x-1)

def getFirstPixel(word: Word):
    x = word.getxCorr()
    y = word.getyCorr()
    return(getPixelNr(x,y))

def getPixels(word: Word):
    pxls = []
    if(word.getWordDirection() == Word.HORIZONTAL):
        lastPxl = getFirstPixel(word)
        pxls.append(lastPxl)
        for i in range(1, word.getWordLength()):
            lastPxl += 1
            pxls.append(lastPxl)
    else:
        lastPxl = getFirstPixel(word)
        pxls.append(lastPxl)
        for i in range(1, word.getWordLength()):
            lastPxl += num_columns
            pxls.append(lastPxl)
    return pxls

def lightUpWords(color = ([255,255,255]), *words):
    for word in words[0]: 
        if(word.getWordDirection() == Word.HORIZONTAL):
            first = getFirstPixel(word)
            last = getFirstPixel(word) + word.getWordLength()
            pixels[first:last] = [color] * word.getWordLength()

        else:
            first = getFirstPixel(word)
            last = getFirstPixel(word) + (word.getWordLength()) * num_columns
            pixels[first:last:num_columns] = [color] * word.getWordLength()

        
def getHour(hour) -> Word:
    switcher = {
        1: eis,
        2: zwöi,
        3: drüü,
        4: vieri,
        5: füfi,
        6: sächsi,
        7: sibni,
        8: achti,
        9: nüni,
        10: zäni,
        11: eufi,
        12: zwöufi
    }
    return switcher.get(hour)

def getTimePhrase(time) -> Word:
    words = []
    if(bool(random.getrandbits(1)) or runType=="fastrun"):
      words = [es, ischzit]
    hNow = getHour(int(time.strftime("%I")))
    h1h = getHour((int(time.strftime("%I"))%12)+1)
    min = int(time.strftime("%M"))

    changeBrightness(time)

    if(min<3):
        words += [hNow]
    elif(min >= 3 and 8 > min):
        words += [füf, ab, hNow]
    elif(min >= 8 and 12 > min):
        words += [zäh, ab, hNow]
    elif(min >= 12 and 17 > min):
        words += [viertu, ab, hNow]
    elif(min >= 17 and 22 > min):
        words +=  [zwänzg, ab, hNow]
    elif(min >= 22 and 27 > min):
        words +=  [füf, vor, haubi, h1h]
    elif(min >= 27 and 32 > min):
        words +=  [haubi, h1h]
    elif(min >= 32 and 37 > min):
        words +=  [füf, ab, haubi, h1h]
    elif(min >= 37 and 42 > min):
        words +=  [zwänzg, vor, h1h]
    elif(min >= 42 and 47 > min):
        words +=  [viertu, vor, h1h]
    elif(min >= 47 and 52 > min):
        words +=  [zäh, vor, h1h]
    elif(min >= 52 and 57 > min):
        words +=  [füf, vor, h1h]
    elif(min >= 57 and 60 > min):
        words +=  [h1h]
    return words

def changeBrightness(time):
    hour = int(time.strftime("%H"))
    print(hour)
    if( hour >= 23 or (hour > 3 and hour < 5)):
        pixels.brightness = 0.03
    elif( hour <= 3):
        pixels.brightness = 0.015
    else:
        pixels.brightness = 0.10


def setTimeOnClock(words, pixels: neopixel.NeoPixel):
    pixels.fill((0,0,0))
    lightUpWords((255,255,255), words)

if len(sys.argv) > 1:
    runType = sys.argv[1]
if len(sys.argv) > 2:
    print(sys.argv[2])
    pixels.brightness = float(sys.argv[2])

if(runType == "startup"):
    Still.heart(pixels)
    time.sleep(10)

if(runType == "smiley"):
    Still.smiley(pixels)
    time.sleep(10)

if(runType == "fastrun"):
    wTimeZero = datetime.now()
    for xi in range((60*24)):
        wTime = wTimeZero + timedelta(minutes=xi)
        setTimeOnClock(getTimePhrase(wTime), pixels)
        pixels.show()
        time.sleep(0.02)


if(runType == "happy"):
    print("hallo")

wTime = datetime.now()
setTimeOnClock(getTimePhrase(wTime), pixels)

pixels.show()
