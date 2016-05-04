''' Download Andy the android simulator
'''

import PIL
from PIL import Image
import time
import pyscreenshot as ImageGrab
import pytesseract

# global variables
totalViews = 0
latestViewCount = 0
sameCountCounter = 0
nothingFoundCounter = 0

def resizeImage(im):
	basewidth = 1250
	wpercent = (basewidth / float (im.size[0]))
	hsize = int((float(im.size[1]) * float(wpercent)))
	im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	return im

def screenShot():
	if __name__ == "__main__":
		im = ImageGrab.grab(bbox=(5, 500, 850, 1320)) # bbox=(5, 70, 850, 1320)
		im = im.convert("L")
		big_im = resizeImage(im)
		return big_im

def getViewsWithPytesseract():
	global latestViewCount
	global totalViews
	global sameCountCounter
	global nothingFoundCounter
	print("4 seconds...")
	time.sleep(4)
	im = screenShot()
	s = pytesseract.image_to_string(im, config='-psm 6')
	print s
	if "views" in s != -1:
		for line in s.split("\n"):
			if "views" in line:
				viewCount = int(filter(str.isdigit, line))
				if viewCount == latestViewCount:
					sameCountCounter += 1
					print sameCountCounter
				if sameCountCounter < 6:
					latestViewCount = viewCount
					totalViews += latestViewCount
					print latestViewCount
					print totalViews
					nothingFoundCounter = 0
					getViewsWithPytesseract()
				else:
					print("The total is %s" % totalViews)
	elif "vlews" in s != -1:
		for line in s.split("\n"):
			if "vlews" in line:
				viewCount = int(filter(str.isdigit, line))
				if viewCount == latestViewCount:
					sameCountCounter += 1
					print sameCountCounter
				if sameCountCounter < 6:
					latestViewCount = viewCount
					totalViews += latestViewCount
					print latestViewCount
					print totalViews
					nothingFoundCounter = 0
					getViewsWithPytesseract()
				else:
					print("The total is %s" % totalViews)
	elif "VIEWS" in s != -1:
		for line in s.split("\n"):
			if "vlews" in line:
				viewCount = int(filter(str.isdigit, line))
				if viewCount == latestViewCount:
					sameCountCounter += 1
					print sameCountCounter
				if sameCountCounter < 6:
					latestViewCount = viewCount
					totalViews += latestViewCount
					print latestViewCount
					print totalViews
					nothingFoundCounter = 0
					getViewsWithPytesseract()
				else:
					print("The total is %s" % totalViews)
	else:
		if nothingFoundCounter < 6:
			print "nothing found"
			nothingFoundCounter += 1
			getViewsWithPytesseract()
		else:
			print("The total is %s" % totalViews)

def main():
	global latestViewCount
	global totalViews
	start = time.time()
	totalViews = 0
	latestViewCount = 0
	getViewsWithPytesseract()
	print("--- End: %s seconds ---" % (time.time() - start))

main()
