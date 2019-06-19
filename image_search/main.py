'''
Created on Jul 24, 2012

@author: Admin
'''


from view.fullscreenwrapper2 import *
from androidhelper import Android
import image_api as ia
import file_select as fs
import datetime
import os
import view.pathhelpers as pathhelpers
import sys
import time

droid = Android()


# Main Screen Class
class MainScreen(Layout):
    ims=[]
    ind=0
    def __init__(self):
        #initialize your class data attributes
        
        #load & set your xml
        super(MainScreen,self).__init__(pathhelpers.read_layout_xml("main.xml"),"Ocr")

    def on_show(self):
    	#self.views.tt.add_event(click_EventHandler(self.views.tt,self.get_options))
    	#self.views.lists.set_listitems(["semir","worku","semir","worku","semir","worku"])
        #initialize your layout views on screen_show
        self.views.preview.visibility = "visible"
        self.views.logo.src = pathhelpers.get_drawable_pathname("logo.png")
        self.views.close_app.add_event(click_EventHandler(self.views.close_app,self.cls_app))
        self.views.search.add_event(click_EventHandler(self.views.search,self.search_pic))
        self.views.next.add_event(click_EventHandler(self.views.next,self.next_pic))
        self.views.prev.add_event(click_EventHandler(self.views.prev,self.prev_pic))
    def search_pic(self,view,event ):
        #self.views.take_pic.visibility = "gone"
        #self.views.upload.visibility = "gone"
        
  
  
  
        self.views.preview.visibility = "gone"
        self.views.action.visibility = "gone"
        self.ind=0
        self.ims=[]
        title = 'Searching'
        message = ''
        droid.dialogCreateSpinnerProgress(title, message)
        droid.dialogShow()
        term=self.views.search_box.text
        res= ia.getImages(term,self)
        self.views.preview.src = res[self.ind]
        self.views.preview.visibility = "visible"
        droid.dialogDismiss()
        self.views.action.visibility = "visible"
        self.views.result.text=str(res)
        print res
            
        
        
    def next_pic(self,view,event ):
    	if self.ind < len(self.ims)-1:
    		self.ind += 1
        	self.views.preview.src = self.ims[self.ind]
       
    def prev_pic(self,view,event ):
    	if self.ind > 0:
    		self.ind -= 1
        	self.views.preview.src = self.ims[self.ind]
    
        
        #FullScreenWrapper2App.close_layout()
    def cls_app(self,view,event):
        FullScreenWrapper2App.close_layout()
    def get_options(self,view,event):
    	title = 'GUI Test?'
    	choices=['Continue', 'Skip', 'baz']
    	droid.dialogCreateAlert(title)
    	droid.dialogSetSingleChoiceItems(choices)
    	droid.dialogSetPositiveButtonText('Yay!')
    	droid.dialogShow()
    	response = droid.dialogGetResponse().result
		
    	selected_choices = droid.dialogGetSelectedItems().result
    	print selected_choices
    	self.views.tt.text=choices[selected_choices[0]]
        return True
    def on_close(self):
        pass

if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()
    
