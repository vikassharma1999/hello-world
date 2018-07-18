from kivy.app import App   #import App class from kivy.app module
from kivy.uix.boxlayout import BoxLayout #import BoxLayout class from kivy.uix.boxlayout module
from guest import GuestLayout #import GuestLayout class from guest module
class Home(BoxLayout):#root widget
	def hello(self):
		self.clear_widgets()
		self.add_widget(GuestLayout())
	def back(self):
		self.clear_widgets()
		self.add_widget(Home())
class ChapApp(App):#App class
	pass
if __name__ == '__main__':
	ChapApp().run()#for running purpose