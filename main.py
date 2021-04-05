import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class OMPBox(Widget):
    med = ObjectProperty(None)
    dos = ObjectProperty(None)
    clock = ObjectProperty(None)

 # Get the data from widget above and create schedule 
    def add_med(self):
        self.OMPBox = OMPBox()
        schedule = self.OMPBox.children[-1]
        med_label = Label(text=self.med.text, font_size=15)
        dos_label = Label(text=self.dos.text, font_size=15)
        time_label = Label(text=self.clock.text, font_size=15)
          # give this buttons an on press later
        taked_btn = Button(text='taked!') 
        del_btn = Button(text='delete')
        meds_schedule = BoxLayout(spacing=100, pos=(self.width/2 -
                                                      med_label.width+dos_label.width/2, self.height-120))
        meds_schedule.add_widget(med_label)
        meds_schedule.add_widget(dos_label)
        meds_schedule.add_widget(time_label)
        meds_schedule.add_widget(taked_btn)
        meds_schedule.add_widget(del_btn)
        
        schedule.add_widget(meds_schedule)





class OhMyPills(App):
    def build(self):
        return OMPBox()

if __name__ == '__main__':
   OhMyPills().run()
