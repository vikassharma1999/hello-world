import random

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
class GuestLayout(Screen):
	def send_msg(self):
		greetIn=['hi','hello','namesty']
		greetOut=['hello','how can i help you?']
		msg = self.ids.message.text
		self.ids.chat_logs.text += ("\nUser:->"+msg)
		if msg in greetIn:
			self.ids.chat_logs.text+=("\nBot:->"+random.choice(greetOut))
		else:
			self.ids.chat_logs.text+=("\nBot:-> Sorry!!")

	
			
    
class GuestApp(App): #main app
	pass
if __name__ == '__main__':
	GuestApp().run()