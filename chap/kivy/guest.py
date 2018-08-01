import random
import time
import pyttsx3
import speech_recognition as sr 
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
r=sr.Recognizer()
mic=sr.Microphone()
class GuestLayout(Screen):
	def send_msg(self):
		greetIn=['hi','hello','namesty']
		greetOut=['hello','how can i help you?']
		
		'''r=sr.Recognizer()
		mic=sr.Microphone()
		engine=pyttsx3.init()
		with mic as source:
			audio=r.listen(source)
		ques=r.recognize_google(audio)
		Q=ques.lower()
		if ques=='':
			self.ids.chat_logs.text+=("\nBot:->"+"Nice to meet you!!!")
			engine.say("Nice to meet you")
			engine.runAndWait()
			time.sleep(2)
			#break
		elif Q in greetIn:
			self.ids.chat_logs.text+=("\nBot:->"+random.choice(greetOut))
			engine.say(random.choice(greetOut))
			engine.runAndWait()
		else:
			self.ids.chat_logs.text+=("\nBot:-> Sorry!!")

'''

		

	
			
    
class GuestApp(App): #main app
	pass
if __name__ == '__main__':
	GuestApp().run()
