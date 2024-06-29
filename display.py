import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

def drawText(str):
    RESET_PIN = digitalio.DigitalInOut(board.D4)

    i2c = board.I2C()  # uses board.SCL and board.SDA

    // 根据屏幕大小修改此处参数，此处为128*32
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    oled.fill(0)
    oled.show()

    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

    draw.text((0, 0), str, font=font2, fill=255)

    oled.image(image)
    oled.show()

