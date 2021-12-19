import time
import board
import neopixel
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
    pixel_pin, num_pixels, brightness=0.05, auto_write=True, pixel_order=ORDER
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

def lightUp(word , pixels: neopixel.NeoPixel , color = ([255,255,255])):
    if(word.getWordDirection() == Word.HORIZONTAL):
        first = getFirstPixel(word)
        last = getFirstPixel(word) + word.getWordLength()
        pixels[first:last] = [color] * word.getWordLength()
    else:
        first = getFirstPixel(word)
        last = getFirstPixel(word) + (word.getWordLengt()-1) * num_columns
        pixels[first:last:num_columns] = [color] * word.getWordLength()

    

es = Word("es", 2, 1, Word.HORIZONTAL)
isch = Word("isch", 5, 1, Word.HORIZONTAL)



lightUp(es, pixels)
lightUp(isch, pixels)
