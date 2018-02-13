# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 11:19:22 2017

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
        self.mylabel1 =Label(text='Investment Amount')
        self.invest =TextInput(text='10000')
        self.mylabel2 =Label(text='Yesrs')
        self.years = TextInput(text='3')
        self.mylabel3 =Label(text='Annual Interest Rate')
        self.interest = TextInput(text='3.25')
        self.mylabel4 =Label(text='Future Value')
        self.future = TextInput(text='')
        self.mybutton=Button(text='Calculate')
        
        layout.add_widget(self.mylabel1)
        layout.add_widget(self.invest)
        layout.add_widget(self.mylabel2)
        layout.add_widget(self.years)
        layout.add_widget(self.mylabel3)
        layout.add_widget(self.interest)
        layout.add_widget(self.mylabel4)
        layout.add_widget(self.future)
        layout.add_widget(self.mybutton)
        
        self.mybutton.bind( on_press =self.calculate)
        
        return layout

    def calculate(self,value):
        print 'calculate'
        invest=float(self.invest.text)
        interest=float(self.interest.text)
        years=float(self.years.text)
        future=round(invest*((1+interest/1200.0)**(years*12)),2)
        self.future.text=str(future)
        

if __name__ == '__main__':
    MyApp().run()