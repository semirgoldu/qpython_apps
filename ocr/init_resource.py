import os
import sys
import json
from androidhelper.sl4a import Android
import glob
import time
import urllib

os.environ['PATH'] = os.environ['PATH']+':/data/data/com.termux/files/usr/bin/'
os.environ['SHELL'] = '/data/data/com.termux/files/usr/bin/sh'
os.environ['MKSH'] = '/data/data/com.termux/files/usr/bin/sh'
os.environ['LD_LIBRARY_PATH'] = '/data/data/com.termux/files/usr/lib'
import numpy as np
import cv as cv2
#from PIL import Image as img
#Initialize Android
droid = Android()

import subprocess
def run(args):
	p= subprocess.Popen(args,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p_out, p_err = p.communicate()
	return p_out, p_err 
def take_pic(path,layout):

	
	filet='/sdcard/'+path+'.png'
	
	new_img='/sdcard/'+path+'_new.png'
	pic=droid.cameraInteractiveCapturePicture(filet)
	res = urllib.urlopen(filet)
	image = np.asarray(bytearray(res.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# perform the actual resizing of the image according to scaling_factor
	height, width = image.shape[:2]
	resized = cv2.resize(image, (width/3, height/3), interpolation = cv2.INTER_AREA)
	cv2.imwrite(new_img, resized)
	# Return gray sale image
	#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	print resized
	layout.views.result.text="Processing ..."
	layout.views.preview.src = "file://"+new_img
	time.sleep(3)
	args=['tesseract', '--tessdata-dir', '/data/data/com.termux/files/usr/share', new_img ,'stdout', '-l', 'eng' ,'--psm', '3','--oem','2']
	return run(args)
def upload_pic(path,layout):

	
	filet=path
	fl=path.split(".")[1]
	new_img='/sdcard/'+fl+'_new.png'
	#pic=droid.cameraInteractiveCapturePicture(filet)
	res = urllib.urlopen(filet)
	image = np.asarray(bytearray(res.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# perform the actual resizing of the image according to scaling_factor
	height, width = image.shape[:2]
	resized = cv2.resize(image, (width/3, height/3), interpolation = cv2.INTER_AREA)
	cv2.imwrite(new_img, resized)
	# Return gray sale image
	#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	print resized
	layout.views.result.text="Processing ..."
	layout.views.preview.src = "file://"+new_img
	time.sleep(3)
	args=['tesseract', '--tessdata-dir', '/data/data/com.termux/files/usr/share', new_img ,'stdout', '-l', 'eng' ,'--psm', '3','--oem','2']
	return run(args)