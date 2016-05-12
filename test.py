# import PIL
# from PIL import Image
# from PIL import ImageGrab
# import time
# import pyautogui
# import pytesseract
import re

def test():
	text = "> 48 views 58k"
	result = int(re.search(r'\d+', text).group())
	print result * 2

test()
