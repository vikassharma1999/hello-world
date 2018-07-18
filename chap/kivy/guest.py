import random

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
class GuestLayout(BoxLayout):
	user_input=ObjectProperty() #object property for store input
	bot_output=ObjectProperty()
	def Namesty(self):
		'''df=pd.read_csv('CS.csv')
		print(df)'''
		greetIn=['hi','hello','namesty']
		greetOut=['hello','how can i help you?']
		self.user_input.text=self.user_input.text.lower()
		if self.user_input.text in greetIn:
			self.bot_output.text=random.choice(greetOut) 
		else:
			self.bot_output.text="I didn't get what you say please try again!!"
	def clear(self):#for reset button
		self.user_input.text=""
		self.bot_output.text=""
	
			
    
class GuestApp(App): #main app
	pass
if __name__ == '__main__':
	GuestApp().run()