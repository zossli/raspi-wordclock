import board
import neopixel

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D18
# Update to match the number of NeoPixels you have connected
pixel_num = 144

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

for i in range(0,144):
    pixels[i]=((int(heart[i])*255),(int(heart[i])*255),0)
pixels.write()