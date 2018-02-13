from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.togglebutton import ToggleButton
from firebase import firebase

url = "https://my-awesome-project-2fdd3.firebaseio.com//" 
token = "P6WgJAORwZYOtqNNz7PFtOB40fbhfSmCN3x0wj7z"
firebase=firebase.FirebaseApplication(url,token)

class GuiKivy(App):

    def build(self):
        layout= GridLayout(cols=2,rows=2)
        # add your widget to the layout
        self.YellowLed = Label(text="Yellow Led", Font_size=24)
        layout.add_widget(self.YellowLed)
        self.Yellowbtn = ToggleButton(text ="Off",on_press=self.updateStatus,state='normal')
        layout.add_widget(self.Yellowbtn)
        self.RedLed = Label(text = "Red Led", Font_size = 24)
        layout.add_widget(self.RedLed)
        self.Redbtn = ToggleButton(text ="Off",on_press=self.updateStatus,state='normal')
        layout.add_widget(self.Redbtn)
        return layout

    def updateStatus(self, instance):
        # use this callback to update firebase
        if self.Yellowbtn.state == 'down':
            self.Yellowbtn.text = "On"
        else:
            self.Yellowbtn.text = "Off"

        if self.Redbtn.state == 'down':
            self.Redbtn.text = "On"
        else:
            self.Redbtn.text = "Off"



GuiKivy().run()