''' Download Andy the android simulator
'''

import PIL
from PIL import Image
from PIL import ImageGrab
import time
import pyautogui
#import pyscreenshot as ImageGrab
import pytesseract

# global variables
totalViews = 0
latestViewCount = 0
sameCountCounter = 1
nothingFoundCounter = 0
totalSuccesses = 0
totalRuns = 0

def resizeImage(im):
	basewidth = 1250
	wpercent = (basewidth / float (im.size[0]))
	hsize = int((float(im.size[1]) * float(wpercent)))
	im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	return im

def screenShot():
	#if __name__ == "__main__":
	im = PIL.ImageGrab.grab(bbox=(5, 850, 850, 1320)) # bbox=(5, 70, 850, 1320)
	im = im.convert("L")
	big_im = resizeImage(im)
	return big_im

def saveViews(totalViews, latestViewCount):
	totalViews = totalViews
	print("The total views are %s" % totalViews)
	with open('total_views.txt', 'w+') as f:
		f.write("totalviewcount: " + str(totalViews) + "\nlastviewcount: " + str(latestViewCount))
	exit()

def counterCheck(viewCount, totalViews, latestViewCount):
	global nothingFoundCounter
	global sameCountCounter
	if viewCount == latestViewCount:
		if sameCountCounter == 10:
			saveViews(totalViews, latestViewCount)
		else:
			sameCountCounter += 1
			print ("This value has printed %s times" % sameCountCounter)
			getViewsWithPytesseract()
	else:
		nothingFoundCounter = 0
		sameCountCounter = 1

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def shiftDown():
	print "\nGoing down...\n"
	# counter = 0
	# while counter < 6:
	# 	#time.sleep(0.5)
	# 	pyautogui.press('down')
	# 	counter += 1
	pyautogui.press('down')
	pyautogui.press('down')

def evaluateViews(line):
	global totalSuccesses
	global totalViews
	global latestViewCount

	totalSuccesses += 1
	if hasNumbers(line):
		viewCount = int(filter(str.isdigit, line))
		counterCheck(viewCount, totalViews, latestViewCount)
		latestViewCount = viewCount
		totalViews += latestViewCount
		print ("View count: %s" % latestViewCount)
		print ("Total views: %s" % totalViews)
		print ("Successes: %s" % totalSuccesses)
	getViewsWithPytesseract()

def getViewsWithPytesseract():
	global latestViewCount, totalViews, nothingFoundCounter, totalRuns
	while totalRuns < 1500:
		try:
			print("Runs: %s" % totalRuns)
			totalRuns += 1
			shiftDown()
			#time.sleep(1)
			im = screenShot()
			s = pytesseract.image_to_string(im, config='-psm 6')
			#print s
			if "views" in s != -1:
				for line in s.split("\n"):
					if "views" in line:
						evaluateViews(line)
			elif "vlews" in s != -1:
				for line in s.split("\n"):
					if "vlews" in line:
						evaluateViews(line)
			elif "VIEWS" in s != -1:
				for line in s.split("\n"):
					if "vlews" in line:
						evaluateViews(line)
			else:
				if nothingFoundCounter == 15:
					saveViews(totalViews, latestViewCount)
				else:
					nothingFoundCounter += 1
					print("Nothing found %s times" % nothingFoundCounter)
					getViewsWithPytesseract()
		except Exception, e:
			print ("Something went terribly wrong: %s" % str(e))

def main():
	pyautogui.FAILSAFE = False
	start = time.time()
	print "Pick window"
	time.sleep(3)
	getViewsWithPytesseract()
	print("--- End: %s seconds ---" % (time.time() - start))

main()
