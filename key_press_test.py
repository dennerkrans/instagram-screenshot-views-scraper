import pyautogui
import time

def main():
	print "Pick window!"
	time.sleep(3)
	counter = 0
	while counter < 7:
		time.sleep(1)
		pyautogui.press('down')
		counter += 1
	print "Done!"

main()
