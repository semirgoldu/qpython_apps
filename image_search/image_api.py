import pprint
import androidhelper.sl4a as android
droid = android.Android()
from googleapiclient.discovery import build
import os
import shutil
import time
import urllib
import numpy as np
import cv.cv2 as cv2
import requests
import ssl 
#h = html2text.HTML2Text()
try: 
    _create_unverified_https_context = ssl._create_unverified_context 
except AttributeError: 
    pass
else: 
    ssl._create_default_https_context = _create_unverified_https_context
def downloadImage(directory,url,name):
    


    #response = requests.get(url, stream=True)
    res = urllib.urlopen(url)
    image = np.asarray(bytearray(res.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    #name = url.split('/')[-1]
    cv2.imwrite(directory+'/'+name,image)
def getImages(query,layout=False,index=0):
	
    dircount=len(os.listdir('/sdcard/test-data/'))
    if dircount==0:
        dircount=1
    else:
        dircount=dircount+1
		
    DIR="/sdcard/test-data/s"+str(index)
    if not os.path.exists(DIR):
        os.mkdir(DIR)
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  
  
  
    service2 = build("customsearch", "v1",
            developerKey="AIzaSyCSyQmtA3Ss5HR817bL745LhgrbliGHyRw")


    res = service2.cse().list(
        q=query,
        cx='009777950347258738662:zlhpjqu5uxk',
        searchType='image',
        num="3",
        hl="en",
        #orTerms="ttt",
        #imgType="photo",
        start=1,
        imgSize="medium",
        safe="off",
        #fileType="jpg",
        #filter="1",
        #siteSearch="https://wikipedia.com"
        
    
    ).execute()
    arr=[]

    if not 'items' in res:
        print 'No result !!\nres is: {}'.format(res)
        return arr
    else:
        cnt=1
        for item in res['items']:
        	
            print item['link']
            if cnt==1:
                term=""
            else:
                term=str(cnt)
            lnk= "file://"+DIR+'/1'+term+".jpg"
            print item["title"].encode("utf-8").strip()
            downloadImage(DIR,item['link'],"1"+term+".jpg")
            layout.ims.append(lnk)
            arr.append(lnk)
            
            #if layout:
            	
            	#layout.views.action.visibility=visible
            #p=droid.view(item["link"],"text/html")
            #print p
            
            	
            
            time.sleep(3)
            cnt=cnt+1
        return arr
subjects=["Denzel Washington","Shakira","Niki Minaj","Johhny Depp"]
index=1
for x in subjects:
    #print "Starting %s" % x   
    #getImages(x+" photo",False,index)
    index += 1
