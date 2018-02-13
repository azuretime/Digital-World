# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 10:51:17 2017

@author: Jiang Jinjing
"""
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.mylabel = Label(text='Apple',
                             color=(1,0,0,1),
                             font_size = 24)
        self.state=0
        self.mylabel.bind( on_touch_down =self.alternate)
        return self.mylabel
    
    def alternate(self,instance,touch):
        if self.state == 0:
            self.state = 1
            self.mylabel.text = 'Juice'
            self.mylabel.color = (0,1,1,1)
            print 'to blue'
        elif self.state==1:
            self.state = 0
            self.mylabel.text = 'Apple'
            self.mylabel.color = (1,0,0,1)
            print 'to red'
            
  
if __name__=="__main__":
    MyApp().run()