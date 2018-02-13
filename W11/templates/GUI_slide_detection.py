# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 11:07:07 2017

@author: Jiang Jinjing
"""

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.mylabel = Label(text='Slide Me',
                             color=(1,0,0,1),
                             font_size = 24)
        self.state=0
        self.mylabel.bind( on_touch_move =self.detect)
        return self.mylabel
    
    def detect(self,instance,touch):
        if touch.dx>0:
            self.mylabel.text = 'Right'
            self.mylabel.color = (0,1,1,1)

        elif touch.dx<0:
            self.mylabel.text = 'Left'
            self.mylabel.color = (0,1,0,1)
            
        elif touch.dy>0:
            self.mylabel.text = 'Up'
            self.mylabel.color = (0,1,1,1)
            
        elif touch.dy<0:
            self.mylabel.text = 'Down'
            self.mylabel.color = (0,1,0,1)
  
if __name__=="__main__":
    MyApp().run()