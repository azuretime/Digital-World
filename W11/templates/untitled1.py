# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 10:21:41 2017

@author: Jiang Jinjing
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyApp(App):

    def build(self):
        layout = GridLayout(cols=2)
        self.mylabel =Label(text='Frequency (Hz)')
        self.frequency =TextInput(text='100.0')
        self.mybutton=Button(text='Calculate period')
        self.result=Label(text='***')
        
        layout.add_widget(self.mylabel)
        layout.add_widget(self.frequency)
        layout.add_widget(self.mybutton)
        layout.add_widget(self.result)
        
        self.mybutton.bind( on_press =self.calculateperiod)
        
        return layout

    def calculateperiod(self,value):
        print 'calculate period'
        frequency=float(self.frequency.text)
        period=1/frequency
        self.result.text=str(period)
        

if __name__ == '__main__':
    MyApp().run()